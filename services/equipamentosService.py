if __name__ == "__main__":
    
    # Garantir funcionamento de imports relativos
    # Utilizado para testes independentes deste módulo
    import os
    import sys

    if __package__ is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)
        if parent_dir not in sys.path:
            sys.path.insert(0, parent_dir)

from database import Database

class EquipamentosService:
    def __init__(self):
        self.database = Database()
        self.database.setDatabase("GEMA") #Define o banco de dados como GEMA
        self.database.setCollection("Equipamentos") #Define a coleção como Equipamentos

    #Busca todos os equipamentos no banco de dados e retorna uma lista de tuplas com as informações relevantes
    def obterTodosEquipamentos(self):

        equipamentos = []

        for equipamento in self.database.getAllItems():
            equipamentos.append((equipamento["_id"], equipamento["descr"], equipamento["serialNum"], equipamento["marca"], equipamento["modelo"], equipamento["observacoes"], equipamento["status"]))

        return equipamentos
    # Obtém um equipamento pelo seu ID e retorna um dicionário com suas informações
    def obterEquipamentoPorID(self, id):
        return self.database.getItemByID(id)
    # Atualiza as informações de um equipamento pelo seu ID 
    def atualizarEquipamentoPorID(self, id, atualizacoes):
        return self.database.updateItemByID(id, atualizacoes)
    

if __name__ == "__main__":
    service = EquipamentosService() #
    equipamentos = service.obterTodosEquipamentos()#obtém todos os equipamentos do banco de dados
    for equipamento in equipamentos:
        print(equipamento)