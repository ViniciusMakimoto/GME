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

    def obterTodasManutencoes(self):

        manutencoes = []

        for manutencao in self.database.getAllItems():
            manutencoes.append((str(manutencao["_id"]), manutencao["id_equipamento"], manutencao["prioridade"], manutencao["tipo"], manutencao["descricao_problema"], manutencao["status"]))

        return manutencoes

    def obterManutencaoPorID(self, id):
        return self.database.getItemByID(id)

    def atualizarManutencaoPorID(self, id, atualizacoes):
        return self.database.updateItemByID(id, atualizacoes)
    

if __name__ == "__main__":
    service = ManutencoesService()
    manutencoes = service.obterTodasManutencoes()
    for manutencao in manutencoes:
        print(manutencao)