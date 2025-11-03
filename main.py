
import tkinter as tk
from tkinter import ttk

from userInterfaces.abaEquipamentos import AbaEquipamentos
from userInterfaces.abaManutencoes import AbaManutencoes

MAIN_BACKGROUND_COLOR = "#252F60"
LATERAL_MENU_COLOR = "#353F6E"


class mainApp:

    def __init__(self, root):

        self.root = root
        self.root.title("GEMA")
        self.root.state("zoomed")  # Janela maximizada

        self.menuLateral = tk.Frame(self.root, width=250, bg=LATERAL_MENU_COLOR)
        self.menuLateral.pack(side="left", fill="y")

        self.botaoEquipamentos = tk.Button(self.menuLateral, text="Equipamentos", command=self.onOpenEquipamentos)
        self.botaoEquipamentos.pack(pady=10, padx=10)

        self.botaoManutencoes = tk.Button(self.menuLateral, text="Manutenções", command=self.onOpenManutencoes)
        self.botaoManutencoes.pack(pady=10, padx=10)

        self.areaPrincipal = tk.Frame(self.root, bg=MAIN_BACKGROUND_COLOR)
        self.areaPrincipal.pack(side="right", expand=True, fill="both")

        self.AbaEquipamentos = AbaEquipamentos(self.areaPrincipal)
        self.AbaManutencoes = AbaManutencoes(self.areaPrincipal)

        self.onOpenEquipamentos()

    def onOpenEquipamentos(self):
        if self.AbaEquipamentos.mainFrame.winfo_ismapped():
            return
        
        self.AbaEquipamentos.mainFrame.pack(expand=True, fill="both")
        self.AbaManutencoes.mainFrame.pack_forget()

    def onOpenManutencoes(self):
        if self.AbaManutencoes.mainFrame.winfo_ismapped():
            return
        
        self.AbaManutencoes.mainFrame.pack(expand=True, fill="both")
        self.AbaEquipamentos.mainFrame.pack_forget()

    def criarTabela(self):
        # Exemplo de criação de tabela usando Treeview
        self.tabela = ttk.Treeview(self.tabelaFrame, columns=("col1", "col2", "col3", "col4", "col5"), show="headings")
        self.tabela.heading("col1", text="Coluna 1")
        self.tabela.heading("col2", text="Coluna 2")
        self.tabela.heading("col3", text="Coluna 3")
        self.tabela.heading("col4", text="Coluna 4")
        self.tabela.heading("col5", text="Coluna 5")
        self.tabela.pack(expand=True, fill='both')

    def atualizarTabela(self, dados):
        # Limpa a tabela existente
        for item in self.tabela.get_children():
            self.tabela.delete(item)
        # Adiciona novos dados à tabela
        for linha in dados:
            self.tabela.insert("", tk.END, values=linha)


if __name__ == "__main__":
    root = tk.Tk()
    app = mainApp(root)
    root.mainloop()