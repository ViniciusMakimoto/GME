
import tkinter as tk
from tkinter import ttk

from services.manutencoesService import ManutencoesService

MAIN_BACKGROUND_COLOR = "#252F60"
LATERAL_MENU_COLOR = "#353F6E"

STATUS_OPTIONS = ["Pendente", "Em Andamento", "Concluído", "Cancelado"]
PRIORIDADE_OPTIONS = ["Baixa", "Média", "Alta"]
TIPO_OPTIONS = ["Preventiva", "Corretiva"]

class AbaManutencoes:
    # definição do construtor da classe
    def __init__(self, areaPrincipal, nova_manutencao_callback, editar_manutencao_callback):
        # Armazena os callbacks para criar nova manutenção e editar manutenção
        self.nova_manutencao_callback = nova_manutencao_callback
        self.editar_manutencao_callback = editar_manutencao_callback

        self.mainFrame = tk.Frame(areaPrincipal, bg=MAIN_BACKGROUND_COLOR)
        
        self.filtroFrame = tk.Frame(self.mainFrame, height=125, bg=MAIN_BACKGROUND_COLOR)
        self.filtroFrame.pack(side="top", fill="x")
        
        self.label = tk.Label(self.filtroFrame, text="Manutenções", font=("Arial", 20), bg="#252F60", fg="white")
        self.label.pack(side="top", fill="x", pady=(20, 0))
        # Chama o método responsável por criar os campos de filtro da tela
        self.criarFiltros()
        
        self.tabelaFrame = tk.Frame(self.mainFrame, bg=MAIN_BACKGROUND_COLOR)
        self.tabelaFrame.pack(side="bottom", expand=True, fill="both")
        # chamada do método que cria a tabela de manutenções
        self.criarTabela()
        # Instancia o serviço de manutenções e carrega os dados iniciais na tabela
        self.manutencoesService = ManutencoesService()
        self.atualizarTabela(self.manutencoesService.obterTodasManutencoes())
    # função que cria os campos de filtro da tela de manutenções
    def criarFiltros(self):

        self.statusLabel = tk.Label(self.filtroFrame, text="Status:",  height=7, bg=MAIN_BACKGROUND_COLOR, fg="white")
        self.statusLabel.pack(side="left", padx=10, pady=10)
        # Cria a lista de opções para o combobox de status, incluindo a opção 'Todos' no início
        statusValues = STATUS_OPTIONS.copy()        # O método .copy() faz uma cópia para não alterar a lista original
        statusValues.insert(0, 'Todos')
        #
        self.statusComboBox = ttk.Combobox(self.filtroFrame, state= "readonly", values=statusValues)
        self.statusComboBox.current(0)
        self.statusComboBox.pack(side="left", padx=10, pady=10)

        self.prioridadeLabel = tk.Label(self.filtroFrame, text="Prioridade:",  height=7, bg=MAIN_BACKGROUND_COLOR, fg="white")
        self.prioridadeLabel.pack(side="left", padx=10, pady=10)

        prioridadeValues = PRIORIDADE_OPTIONS.copy()
        prioridadeValues.insert(0, 'Todas')

        self.prioridadeComboBox = ttk.Combobox(self.filtroFrame, state= "readonly", values=prioridadeValues) #Readonly impede digitação manual, apenas seleção
        self.prioridadeComboBox.current(0)
        self.prioridadeComboBox.pack(side="left", padx=10, pady=10)

        self.tipoLabel = tk.Label(self.filtroFrame, text="Tipo:",  height=7, bg=MAIN_BACKGROUND_COLOR, fg="white")
        self.tipoLabel.pack(side="left", padx=10, pady=10)

        tipoValues = TIPO_OPTIONS.copy()
        tipoValues.insert(0, 'Todos')

        self.tipoComboBox = ttk.Combobox(self.filtroFrame, state= "readonly", values=tipoValues)
        self.tipoComboBox.current(0)
        self.tipoComboBox.pack(side="left", padx=10, pady=10)

        self.pesquisaLabel = tk.Label(self.filtroFrame, text="Pesquisar (id):", bg=MAIN_BACKGROUND_COLOR, fg="white")
        self.pesquisaLabel.pack(side="left", padx=10, pady=10)

        self.pesquisaEntry = tk.Entry(self.filtroFrame)
        self.pesquisaEntry.pack(side="left", padx=10, pady=10)
        
        self.pesquisaEntry.bind('<Return>', self.onAplicarFiltro)

        self.aplicarFiltroButton = tk.Button(self.filtroFrame, text="Aplicar Filtro", command=self.onAplicarFiltro)
        self.aplicarFiltroButton.pack(side="left", padx=10, pady=10)

        self.botCriarManutencao = tk.Button(self.filtroFrame, text="Nova Manutenção", command=self.onCriarManutencao)
        self.botCriarManutencao.pack(side="right", padx=10, pady=10)
    
    def on_double_click(self, event):
        selected_item = self.tabela.selection()
        if selected_item:
            # O método selection() retorna uma tupla, pegue o primeiro elemento
            item_id = selected_item[0]
            print(f"Item clicado duas vezes: {item_id}")
            # obtém os valores da linha 
            values = self.tabela.item(item_id, 'values')
            manutecao_id = values[0] if values else None
            # Se houver callback, abre a aba de manutenções e aplica o filtro por id
            if manutecao_id and self.editar_manutencao_callback:
                self.editar_manutencao_callback(manutecao_id)

    def onCriarManutencao(self):
        self.nova_manutencao_callback()
    # Aplica os filtros selecionados na tela de manutenções
    def onAplicarFiltro(self, event=None):
        todosEquipamentos = self.manutencoesService.obterTodasManutencoes()
        statusSelecionado = self.statusComboBox.get()
        prioridadeSelecionada = self.prioridadeComboBox.get()
        tipoSelecionado = self.tipoComboBox.get()
        pesquisaTexto = self.pesquisaEntry.get().strip()

        if statusSelecionado == "Todos":
            filtro = todosEquipamentos
        else:
            filtro = [equip for equip in todosEquipamentos if equip[5].lower() == statusSelecionado.lower()]

        if prioridadeSelecionada != "Todas":
            #Crie uma nova lista com todos os itens equip de filtro onde o valor na posição 2 (prioridade) for igual à prioridade selecionada no filtro da tela
            filtro = [equip for equip in filtro if equip[2].lower() == prioridadeSelecionada.lower()]

        if tipoSelecionado != "Todos":
            filtro = [equip for equip in filtro if equip[3].lower() == tipoSelecionado.lower()]

        if pesquisaTexto != "":
            def id_match(equip, pesquisa):
                id_str = str(equip[1])
                
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
                    return pesquisaTexto.lower() in str(equip[1]).lower()
                
                return False
            #cria uma nova lista com todos os itens equip de filtro onde o id corresponde ao texto pesquisado
            filtro = [equip for equip in filtro if id_match(equip, pesquisaTexto)]

        
        self.atualizarTabela(filtro)
    
    def abrirComFiltroPorId(self, equip_id):
        """
        Abre a aba de manutenções já filtrada pelo ID do equipamento.
        Usa o campo 'ID Equipamento'.
        """
        todos = self.manutencoesService.obterTodasManutencoes()
        
        # Reseta filtros
        self.statusComboBox.current(0)
        self.prioridadeComboBox.current(0)
        self.tipoComboBox.current(0)
        self.pesquisaEntry.delete(0, tk.END)

        # atualiza campo de pesquisa
        filtro = [m for m in todos if str(m[1]) == str(equip_id)]
        self.pesquisaEntry.insert(0, str(equip_id))

        # mostra resultados filtrados
        self.atualizarTabela(filtro)

    def criarTabela(self):
        columns = ("col1", "col2", "col3", "col4", "col5", "col6")

        self.tabela = ttk.Treeview(self.tabelaFrame, columns= columns, show="headings")
        self.tabela.heading("col1", text="ID")
        self.tabela.heading("col2", text="ID Equipamento")
        self.tabela.heading("col3", text="Prioridade")
        self.tabela.heading("col4", text="Tipo")
        self.tabela.heading("col5", text="Descrição do Problema")
        self.tabela.heading("col6", text="Status")
        self.tabela.pack(expand=True, fill='both')

        for col in columns:
            self.tabela.column(col, anchor=tk.CENTER)

        self.tabela.bind('<Double-1>', self.on_double_click)

    def atualizarTabela(self, dados):

        # Limpa a tabela existente
        for item in self.tabela.get_children():
            self.tabela.delete(item)

        # Substitui valores None ou "" por "-"
        dados = [[valor if valor not in (None, "") else "-" for valor in linha] for linha in dados]

        # Adiciona novos dados à tabela
        for linha in dados:
            self.tabela.insert("", tk.END, values=linha)