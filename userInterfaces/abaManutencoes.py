
import tkinter as tk
from tkinter import ttk

MAIN_BACKGROUND_COLOR = "#252F60"
LATERAL_MENU_COLOR = "#353F6E"

class AbaManutencoes:
    def __init__(self, areaPrincipal):

        self.mainFrame = tk.Frame(areaPrincipal, bg=MAIN_BACKGROUND_COLOR)
        
        self.filtroFrame = tk.Frame(self.mainFrame, height=125, bg=MAIN_BACKGROUND_COLOR)
        self.filtroFrame.pack(side="top", fill="x")

        self.tabelaFrame = tk.Frame(self.mainFrame, bg=MAIN_BACKGROUND_COLOR)
        self.tabelaFrame.pack(side="bottom", expand=True, fill="both")

        self.criarTabela()
        self.atualizarTabela([
            ("Dado 1", "Dado 2", "Dado 3"),
            ("Dado A", "Dado B", "Dado C"),
            ("Info 1", "Info 2", "Info 3")])
    
    def criarTabela(self):
        # Exemplo de criação de tabela usando Treeview
        self.tabela = ttk.Treeview(self.tabelaFrame, columns=("col1", "col2", "col3"), show="headings")
        self.tabela.heading("col1", text="Coluna 1")
        self.tabela.heading("col2", text="Coluna 2")
        self.tabela.heading("col3", text="Coluna 3")
        self.tabela.pack(expand=True, fill='both')

    def atualizarTabela(self, dados):
        # Limpa a tabela existente
        for item in self.tabela.get_children():
            self.tabela.delete(item)
        # Adiciona novos dados à tabela
        for linha in dados:
            self.tabela.insert("", tk.END, values=linha)