
import tkinter as tk
from tkinter import ttk

from services.equipamentosService import EquipamentosService

MAIN_BACKGROUND_COLOR = "#252F60"
LATERAL_MENU_COLOR = "#353F6E"

class AbaEquipamentos:
    def __init__(self, areaPrincipal):

        self.mainFrame = tk.Frame(areaPrincipal, bg=MAIN_BACKGROUND_COLOR)
        
        self.filtroFrame = tk.Frame(self.mainFrame, height=125, bg=MAIN_BACKGROUND_COLOR)
        self.filtroFrame.pack(side="top", fill="x")

        self.tabelaFrame = tk.Frame(self.mainFrame, bg=MAIN_BACKGROUND_COLOR)
        self.tabelaFrame.pack(side="bottom", expand=True, fill="both")

        self.criarTabela()
        self.atualizarTabela([
            ("1", "SN12345", "MarcaA", "ModeloX", "Nenhum", "Ativo"),
            ("2", "SN67890", "MarcaB", "ModeloY", "Revisão necessária", "Inativo"),
            ("3", "SN54321", "MarcaC", "ModeloZ", "Em uso", "Ativo")])
        
        self.equipamentosService = EquipamentosService()
        #self.atualizarTabela(self.equipamentosService.obterTodosEquipamentos())

    def criarTabela(self):
        # Exemplo de criação de tabela usando Treeview
        self.tabela = ttk.Treeview(self.tabelaFrame, columns=("col1", "col2", "col3", "col4", "col5", "col6"), show="headings")
        self.tabela.heading("col1", text="ID")
        self.tabela.heading("col2", text="Serial Number")
        self.tabela.heading("col3", text="Marca")
        self.tabela.heading("col4", text="Modelo")
        self.tabela.heading("col5", text="Observações")
        self.tabela.heading("col6", text="Status")
        self.tabela.pack(expand=True, fill='both')

    def atualizarTabela(self, dados):

        # Limpa a tabela existente
        for item in self.tabela.get_children():
            self.tabela.delete(item)
        # Adiciona novos dados à tabela
        for linha in dados:
            self.tabela.insert("", tk.END, values=linha)