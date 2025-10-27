import pymongo
import json
from datetime import datetime

class DatabaseManager:
    """
    Classe responsável por toda a interação com o banco de dados MongoDB.
    Implementa o Single Responsibility Principle (SRP) ao focar apenas
    nas operações de banco de dados.
    """

    def __init__(self, connection_string="mongodb://localhost:27017/", db_name="lab_66"):
        """
        Inicializa a conexão com o MongoDB.

        Args:
            connection_string (str): String de conexão do MongoDB.
            db_name (str): Nome do banco de dados a ser utilizado.
        """
        try:
            self.client = pymongo.MongoClient(connection_string)
            self.db = self.client[db_name]
            self.equip_collection = self.db["equipamentos"]
            self.maint_collection = self.db["manutencoes"]
            print(f"Conectado ao MongoDB (DB: {db_name}) com sucesso.")
        except pymongo.errors.ConnectionFailure as e:
            print(f"Erro ao conectar ao MongoDB: {e}")
            raise

    def import_initial_data(self, json_file_path):
        """
        Importa os dados iniciais do arquivo JSON para a coleção 'equipamentos'.
        Utiliza 'update_one' com 'upsert=True' para evitar duplicatas
        se o script for executado múltiplas vezes (idempotência).

        Args:
            json_file_path (str): Caminho para o arquivo JSON.
        
        Returns:
            int: Número de novos documentos inseridos.
        """
        try:
            with open(json_file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            inserted_count = 0
            for item in data:
                # Adiciona um campo de histórico de manutenção vazio se não existir
                item.setdefault('historico_manutencao', [])
                
                result = self.equip_collection.update_one(
                    {"_id": item["_id"]},
                    {"$setOnInsert": item},
                    upsert=True
                )
                if result.upserted_id:
                    inserted_count += 1
            
            print(f"{inserted_count} novos equipamentos importados.")
            return inserted_count
        except FileNotFoundError:
            print(f"Erro: Arquivo JSON não encontrado em '{json_file_path}'")
            return 0
        except Exception as e:
            print(f"Erro ao importar dados: {e}")
            return 0

    def get_all_equipments(self):
        """Retorna todos os equipamentos da coleção."""
        try:
            return list(self.equip_collection.find())
        except Exception as e:
            print(f"Erro ao buscar equipamentos: {e}")
            return []

    def find_equipment_by_id(self, equip_id):
        """
        Busca um equipamento específico pelo seu _id.
        Tenta converter o ID para int, se falhar, usa como string.
        """
        try:
            # Tenta converter o ID para inteiro, pois o JSON usa int
            try:
                query_id = int(equip_id)
            except ValueError:
                query_id = equip_id # Usa como string se não for int
                
            return self.equip_collection.find_one({"_id": query_id})
        except Exception as e:
            print(f"Erro ao buscar equipamento por ID '{equip_id}': {e}")
            return None

    def add_maintenance_record(self, equip_id, tipo, responsavel, descricao):
        """
        Cria um novo registro de manutenção e o associa a um equipamento.
        
        Args:
            equip_id (int or str): O _id do equipamento.
            tipo (str): Tipo de manutenção (ex: Corretiva, Preventiva).
            responsavel (str): Nome do técnico.
            descricao (str): Detalhes da manutenção.
            
        Returns:
            ObjectId: O ID do novo registro de manutenção, ou None se falhar.
        """
        try:
            maintenance_doc = {
                "equip_id": equip_id,
                "data": datetime.now(),
                "tipo": tipo,
                "responsavel": responsavel,
                "descricao": descricao
            }
            result = self.maint_collection.insert_one(maintenance_doc)
            return result.inserted_id
        except Exception as e:
            print(f"Erro ao adicionar registro de manutenção: {e}")
            return None

    def update_equipment_status(self, equip_id, new_status, observacao):
        """
        Atualiza o status e as observações de um equipamento.

        Args:
            equip_id (int or str): O _id do equipamento.
            new_status (str): O novo status (ex: "Disponível", "Manutenção").
            observacao (str): Nova observação.
        
        Returns:
            bool: True se a atualização foi bem-sucedida, False caso contrário.
        """
        try:
            result = self.equip_collection.update_one(
                {"_id": equip_id},
                {"$set": {"status": new_status, "observacoes": observacao}}
            )
            return result.modified_count > 0
        except Exception as e:
            print(f"Erro ao atualizar status do equipamento {equip_id}: {e}")
            return False

    def get_maintenance_history_by_equip_id(self, equip_id):
        """
        Retorna o histórico de manutenções de um equipamento específico.
        """
        try:
            return list(self.maint_collection.find({"equip_id": equip_id}).sort("data", -1))
        except Exception as e:
            print(f"Erro ao buscar histórico do equipamento {equip_id}: {e}")
            return []

    def get_status_report(self):
        """
        Gera um relatório de contagem de equipamentos por status.
        Utiliza o pipeline de agregação do MongoDB.
        
        Returns:
            list: Lista de dicionários (ex: [{'_id': 'Disponível', 'count': 50}]).
        """
        try:
            pipeline = [
                {"$group": {"_id": "$status", "count": {"$sum": 1}}},
                {"$sort": {"_id": 1}}
            ]
            return list(self.equip_collection.aggregate(pipeline))
        except Exception as e:
            print(f"Erro ao gerar relatório de status: {e}")
            return []
