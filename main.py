
import tkinter as tk
from tkinter import ttk

from userInterfaces.abaEquipamentos import AbaEquipamentos
from userInterfaces.abaManutencoes import AbaManutencoes
from userInterfaces.abaNovaManutencao import AbaNovaManutencao

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

        self.AbaEquipamentos = AbaEquipamentos(self.areaPrincipal, abrir_manutencoes_callback=self.abrirManutencoesComFiltro)
        self.AbaManutencoes = AbaManutencoes(self.areaPrincipal, nova_manutencao_callback=self.onOpenNovaManutencao)
        self.AbaNovaManutencao = AbaNovaManutencao(self.areaPrincipal)

        self.onOpenEquipamentos()

    def onOpenEquipamentos(self):
        if self.AbaEquipamentos.mainFrame.winfo_ismapped():
            return
        
        self.AbaEquipamentos.mainFrame.pack(expand=True, fill="both")
        self.AbaManutencoes.mainFrame.pack_forget()
        self.AbaNovaManutencao.mainFrame.pack_forget()

    def onOpenManutencoes(self):
        if self.AbaManutencoes.mainFrame.winfo_ismapped():
            return
        
        self.AbaManutencoes.mainFrame.pack(expand=True, fill="both")
        self.AbaEquipamentos.mainFrame.pack_forget()
        self.AbaNovaManutencao.mainFrame.pack_forget()

    def abrirManutencoesComFiltro(self, equip_id):
        self.AbaManutencoes.abrirComFiltroPorId(equip_id)
        self.onOpenManutencoes()

    def onOpenNovaManutencao(self):
        if self.AbaNovaManutencao.mainFrame.winfo_ismapped():
            return
        
        self.AbaNovaManutencao.resetOptions()
        self.AbaNovaManutencao.mainFrame.pack(expand=True, fill="both")
        self.AbaManutencoes.mainFrame.pack_forget()
        self.AbaEquipamentos.mainFrame.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = mainApp(root)
    root.mainloop()