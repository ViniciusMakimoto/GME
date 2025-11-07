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

class ManutencoesService:
    def __init__(self):
        self.database = Database()
        self.database.setDatabase("GEMA")
        self.database.setCollection("Manutencoes")
    #Busca todas as manutenções no banco de dados e retorna uma lista de tuplas com as informações relevantes
    def obterTodasManutencoes(self):

        manutencoes = []

        for manutencao in self.database.getAllItems():
            manutencoes.append((str(manutencao["_id"]), manutencao["id_equipamento"], manutencao["prioridade"], manutencao["tipo"], manutencao["descricao_problema"], manutencao["status"]))

        return manutencoes
    # Obtém uma manutenção pelo seu ID e retorna um dicionário com suas informações
    def obterManutencaoPorID(self, id):
        return self.database.getItemByID(id)
    # Atualiza as informações de uma manutenção pelo seu ID
    def atualizarManutencaoPorID(self, id, atualizacoes):
        return self.database.updateItemByID(id, atualizacoes)
    # Cria uma nova manutenção no banco de dados
    def criarNovaManutencao(self, manutencao_data):
        return self.database.insertItem(manutencao_data)
    

if __name__ == "__main__":
    service = ManutencoesService()
    manutencoes = service.obterTodasManutencoes()
    for manutencao in manutencoes:
        print(manutencao)