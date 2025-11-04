
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
        self.criarFiltros()
        
        self.tabelaFrame = tk.Frame(self.mainFrame, bg=MAIN_BACKGROUND_COLOR)
        self.tabelaFrame.pack(side="bottom", expand=True, fill="both")
        
        self.criarTabela()

        self.equipamentosService = EquipamentosService()
        self.atualizarTabela(self.equipamentosService.obterTodosEquipamentos())

    def criarFiltros(self):

        self.statusLabel = tk.Label(self.filtroFrame, text="Status:",  height=7, bg=MAIN_BACKGROUND_COLOR, fg="white")
        self.statusLabel.pack(side="left", padx=10, pady=10)

        self.statusComboBox = ttk.Combobox(self.filtroFrame, state= "readonly", values=["Todos", "Disponível", "Manutenção"])
        self.statusComboBox.current(0)
        self.statusComboBox.pack(side="left", padx=10, pady=10)

        self.pesquisaLabel = tk.Label(self.filtroFrame, text="Pesquisar (id):", bg=MAIN_BACKGROUND_COLOR, fg="white")
        self.pesquisaLabel.pack(side="left", padx=10, pady=10)

        self.pesquisaEntry = tk.Entry(self.filtroFrame)
        self.pesquisaEntry.pack(side="left", padx=10, pady=10)
        
        self.pesquisaEntry.bind('<Return>', self.onAplicarFiltro)

        self.aplicarFiltroButton = tk.Button(self.filtroFrame, text="Aplicar Filtro", command=self.onAplicarFiltro)
        self.aplicarFiltroButton.pack(side="left", padx=10, pady=10)

    def onAplicarFiltro(self, event=None):
        todosEquipamentos = self.equipamentosService.obterTodosEquipamentos()
        statusSelecionado = self.statusComboBox.get()
        pesquisaTexto = self.pesquisaEntry.get().strip()

        if statusSelecionado == "Todos":
            filtroStatus = todosEquipamentos
        else:
            filtroStatus = [equip for equip in todosEquipamentos if equip[5] == statusSelecionado]
        
        if pesquisaTexto == "":
            filtroPesquisa = filtroStatus
        else:
            def id_match(equip, pesquisa):
                id_str = str(equip[0])
                # Verifica se pesquisa é igual ao id
                if pesquisa.lower() == id_str.lower():
                    return True
                # Verifica se pesquisa contém o id nos últimos 5 até os 3 últimos dígitos
                if len(pesquisa) >= 5:
                    # Extrai os dígitos do 5º ao 3º a partir do final
                    mask_id = pesquisa[-5:-2]
                    if id_str == mask_id:
                        return True
                # Verifica se pesquisa é menor ou igual a 3 caracteres e está contido no id  
                if len(pesquisa) <= 3:
                    return pesquisaTexto.lower() in str(equip[0]).lower()
                
                return False

            filtroPesquisa = [equip for equip in filtroStatus if id_match(equip, pesquisaTexto)]

        self.atualizarTabela(filtroPesquisa)

    def on_double_click(self, event):
        selected_item = self.tabela.selection()
        if selected_item:
            # O método selection() retorna uma tupla, pegue o primeiro elemento
            item_id = selected_item[0]
            print(f"Item clicado duas vezes: {item_id}")
            # Faça o que precisar com o item_id aqui, como obter os valores
            values = self.tabela.item(item_id, 'values')
            print(f"Valores do item: {values}")

    def criarTabela(self):
        columns = ("col1", "col2", "col3", "col4", "col5", "col6")

        self.tabela = ttk.Treeview(self.tabelaFrame, columns= columns, show="headings")
        self.tabela.heading("col1", text="ID")
        self.tabela.heading("col2", text="Serial Number")
        self.tabela.heading("col3", text="Marca")
        self.tabela.heading("col4", text="Modelo")
        self.tabela.heading("col5", text="Observações")
        self.tabela.heading("col6", text="Status")
        self.tabela.pack(expand=True, fill='both')

        for col in columns:
            self.tabela.column(col, anchor=tk.CENTER)

        self.tabela.bind('<Double-1>', self.on_double_click)

    def atualizarTabela(self, dados: list):

        # Limpa a tabela existente
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        # Substitui valores None por ""
        dados = [[valor if valor is not None else "-" for valor in linha] for linha in dados]

        # Adiciona novos dados à tabela
        for linha in dados:
            self.tabela.insert("", tk.END, values=linha)