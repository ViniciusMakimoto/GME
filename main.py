
import tkinter as tk
from tkinter import ttk

from userInterfaces.abaEquipamentos import AbaEquipamentos
from userInterfaces.abaManutencoes import AbaManutencoes
from userInterfaces.abaNovaManutencao import AbaNovaManutencao
from userInterfaces.abaEditarManutencao import AbaEditarManutencao
import os

MAIN_BACKGROUND_COLOR = "#252F60"
LATERAL_MENU_COLOR = "#353F6E"

class mainApp:

    def __init__(self, root):

        self.root = root
        self.root.title("GEMA")
        self.root.state("zoomed")  # Janela maximizada

        self.menuLateral = tk.Frame(self.root, width=350, bg=LATERAL_MENU_COLOR)  # Define a largura do menu lateral para 350 pixels
        self.menuLateral.pack(side="left", fill="y") # Preenche verticalmente o menu lateral

        # Adiciona uma imagem no menu lateral
        self.logo_img = tk.PhotoImage(file=os.path.abspath("images/LogoGEMA.png"))
        self.logo_label = tk.Label(self.menuLateral, image=self.logo_img, bg=LATERAL_MENU_COLOR)
        self.logo_label.grid(row=0, column=0, pady=(30, 10), padx=10, sticky="n")

        # Frame para centralizar os botões
        self.botoes_frame = tk.Frame(self.menuLateral, bg=LATERAL_MENU_COLOR)
        self.botoes_frame.grid(row=1, rowspan=3, column=0, pady=10, padx=30, sticky="nsew")

        self.menuLateral.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)  
        self.menuLateral.grid_columnconfigure(0, weight=1)

        self.botaoEquipamentos = tk.Button(self.botoes_frame, text="Equipamentos", command=self.onOpenEquipamentos, height=2)
        self.botaoEquipamentos.pack(pady=10, fill="x")

        self.botaoManutencoes = tk.Button(self.botoes_frame, text="Manutenções", command=self.onOpenManutencoes, height=2)
        self.botaoManutencoes.pack(pady=10, fill="x")

        self.botaoNovaManutencao = tk.Button(self.botoes_frame, text="Nova Manutenção", command=self.onOpenNovaManutencao, height=2)
        self.botaoNovaManutencao.pack(pady=10, fill="x")

        self.areaPrincipal = tk.Frame(self.root, bg=MAIN_BACKGROUND_COLOR)
        self.areaPrincipal.pack(side="right", expand=True, fill="both")

        # Imagem no final do menu lateral
        self.final_img = tk.PhotoImage(file=os.path.abspath("images/LogoCEFSA.png"))
        self.final_label = tk.Label(self.menuLateral, image=self.final_img, bg=LATERAL_MENU_COLOR)
        self.final_label.grid(row=4, column=0, pady=(10, 30), padx=10, sticky="s")

        self.AbaEquipamentos = AbaEquipamentos(self.areaPrincipal, abrir_manutencoes_callback=self.abrirManutencoesComFiltro)
        self.AbaManutencoes = AbaManutencoes(self.areaPrincipal, nova_manutencao_callback=self.onOpenNovaManutencao, editar_manutencao_callback = self.onOpenEditarManutencao)
        self.AbaNovaManutencao = AbaNovaManutencao(self.areaPrincipal, open_manutencoes_callback=self.abrirManutencoesComFiltro)
        self.AbaEditarManutecao = AbaEditarManutencao(self.areaPrincipal, open_manutencoes_callback=self.abrirManutencoesComFiltro)
        self.onOpenEquipamentos()

    def onOpenEquipamentos(self):
        if self.AbaEquipamentos.mainFrame.winfo_ismapped():
            return
        
        self.AbaEquipamentos.mainFrame.pack(expand=True, fill="both", padx= 20)
        self.AbaManutencoes.mainFrame.pack_forget()
        self.AbaNovaManutencao.mainFrame.pack_forget()
        self.AbaEditarManutecao.mainFrame.pack_forget()

    def onOpenManutencoes(self):
        if self.AbaManutencoes.mainFrame.winfo_ismapped():
            return
        
        self.AbaManutencoes.mainFrame.pack(expand=True, fill="both", padx= 20)
        self.AbaEquipamentos.mainFrame.pack_forget()
        self.AbaNovaManutencao.mainFrame.pack_forget()
        self.AbaEditarManutecao.mainFrame.pack_forget()

    def abrirManutencoesComFiltro(self, equip_id):
        self.AbaManutencoes.abrirComFiltroPorId(equip_id)
        self.onOpenManutencoes()

    def onOpenNovaManutencao(self):
        if self.AbaNovaManutencao.mainFrame.winfo_ismapped():
            return
        
        self.AbaNovaManutencao.mainFrame.pack(expand=True, fill="both", padx= 50)
        self.AbaNovaManutencao.resetOptions()
        self.AbaManutencoes.mainFrame.pack_forget()
        self.AbaEquipamentos.mainFrame.pack_forget()
        self.AbaEditarManutecao.mainFrame.pack_forget()

    def onOpenEditarManutencao(self, manutecao_id):
        if self.AbaEditarManutecao.mainFrame.winfo_ismapped():
            return
        
        isValid = self.AbaEditarManutecao.verificarManutencaoValida(manutecao_id)
        if not isValid:
            return

        self.AbaEditarManutecao.mainFrame.pack(expand=True, fill="both", padx= 50)
        self.AbaEditarManutecao.popularCampos(manutecao_id)
        self.AbaNovaManutencao.mainFrame.pack_forget()
        self.AbaManutencoes.mainFrame.pack_forget()
        self.AbaEquipamentos.mainFrame.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = mainApp(root)
    root.mainloop()