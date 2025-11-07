import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

from services.manutencoesService import ManutencoesService
from services.equipamentosService import EquipamentosService
from bson import ObjectId
import re

class AbaNovaManutencao:
    # definição do construtor da classe
    def __init__(self, areaPrincipal, open_manutencoes_callback):

        self.mainFrame = tk.Frame(areaPrincipal, bg="#252F60")
        
        # Ajusta o grid para expandir os campos corretamente
        self.mainFrame.columnconfigure(0, weight=0)
        self.mainFrame.columnconfigure(1, weight=1)
        self.mainFrame.columnconfigure(2, weight=1)
        self.mainFrame.columnconfigure(3, weight=2)

        self.label = tk.Label(self.mainFrame, text="Registar Nova Manutenção", font=("Arial", 20), bg="#252F60", fg="white")
        self.label.grid(row=0, column=0, columnspan=4, pady=20, sticky="ew")
        #Inicializa os componentes da GUI
        self.initGUI()
        #Instancia o serviço de manutenções
        self.manutencoesService = ManutencoesService()
        #Instancia o serviço de equipamentos
        self.equipamentoService = EquipamentosService()
        #Callback para abrir a aba de manutenções
        self.open_manutencoes_callback = open_manutencoes_callback

    def initGUI(self):
         # ID Equipamento
        lbl_id = tk.Label(self.mainFrame, text="ID Equipamento", bg="#252F60", fg="white")
        lbl_id.grid(row=1, column=0, sticky="w", padx=20, pady=2)

        ent_id = tk.Entry(self.mainFrame, width=18)
        ent_id.grid(row=1, column=1, sticky="ew", padx=5, pady=2)

        # Solicitante
        lbl_solicitante = tk.Label(self.mainFrame, text="Solicitante", bg="#252F60", fg="white")
        lbl_solicitante.grid(row=2, column=0, sticky="w", padx=20, pady=2)

        ent_solicitante = ttk.Combobox(self.mainFrame, values=["Ryan", "Pedro"], width=12)
        ent_solicitante.grid(row=2, column=1, sticky="ew", padx=5, pady=2)

        # Status (combo menor)
        lbl_status = tk.Label(self.mainFrame, text="Status", bg="#252F60", fg="white")
        lbl_status.grid(row=3, column=0, sticky="w", padx=20, pady=2)

        cb_status = ttk.Combobox(self.mainFrame, values=["Pendente", "Em andamento", "Concluída"], state="readonly", width=12)
        cb_status.grid(row=3, column=1, sticky="ew", padx=5, pady=2)

        # Prioridade (combo menor)
        lbl_prioridade = tk.Label(self.mainFrame, text="Prioridade", bg="#252F60", fg="white")
        lbl_prioridade.grid(row=4, column=0, sticky="w", padx=20, pady=2)

        cb_prioridade = ttk.Combobox(self.mainFrame, values=["Baixa", "Média", "Alta"], state="readonly", width=12)
        cb_prioridade.grid(row=4, column=1, sticky="ew", padx=5, pady=2)

        # Tipo (combo menor)
        lbl_tipo = tk.Label(self.mainFrame, text="Tipo", bg="#252F60", fg="white")
        lbl_tipo.grid(row=5, column=0, sticky="w", padx=20, pady=2)

        cb_tipo = ttk.Combobox(self.mainFrame, values=["Corretiva", "Preventiva"], state="readonly", width=12)
        cb_tipo.grid(row=5, column=1, sticky="ew", padx=5, pady=2)

        # Descrição do Problema (campo maior — multi-linha)
        lbl_desc = tk.Label(self.mainFrame, text="Descrição do Problema", bg="#252F60", fg="white")
        lbl_desc.grid(row=6, column=0, sticky="nw", padx=20, pady=2)

        txt_desc = tk.Text(self.mainFrame, height=10, wrap="word")
        txt_desc.grid(row=6, column=1, columnspan=3, sticky="ew", padx=5, pady=2)

        # Botão para salvar
        self.btn_salvar = tk.Button(self.mainFrame, text="Salvar Manutenção", bg="#1E90FF", fg="white", command=self.salvarManutencao)
        self.btn_salvar.grid(row=7, column=1, columnspan=3, sticky="ew", padx=5, pady=2)

        # Armazena referências dos campos para uso posterior
        self.campos = {
            "id_equipamento": ent_id,
            "solicitante": ent_solicitante,
            "prioridade": cb_prioridade,
            "tipo": cb_tipo,
            "descricao_problema": txt_desc,
            "status": cb_status
        }
    # função para resetar os campos do formulário
    def resetOptions(self):
        for chave, widget in self.campos.items():
            if chave == "solicitante":
                widget.set("")
                continue
            
            if isinstance(widget, ttk.Combobox):
                widget.current(0)
            elif isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)
            elif isinstance(widget, tk.Text):
                widget.delete("1.0", tk.END)
    # função para obter os dados do formulário
    def obterDadosFormulario(self):
        dados = {}
        for chave, widget in self.campos.items():
            if isinstance(widget, ttk.Combobox):
                dados[chave] = widget.get().strip()
            elif isinstance(widget, tk.Entry):
                dados[chave] = widget.get().strip()
            elif isinstance(widget, tk.Text):
                dados[chave] = widget.get("1.0", tk.END).strip()

        def getID_Equip(id_equip):
            return id_equip #TODO: FILTRAR MASCARA E OBTER ID VERDADEIRO

        # Aplica a função para extrair o ID sem máscara
        dados["id_equipamento"] = getID_Equip(dados.get("id_equipamento"))

        return dados
    #Função para verificar os campos obrigatórios
    def verificarCamposObrigatorios(self, dados):
        campos_obrigatorios = ["id_equipamento", "solicitante", "descricao_problema"]
        for campo in campos_obrigatorios:
            if not dados.get(campo):
                return False, f"Campo {campo} não pode ser vazio!"
            
        ID_Equipamento = int(dados.get("id_equipamento"))
            
        equipamentoInfo = self.equipamentoService.obterEquipamentoPorID(ID_Equipamento)
        if equipamentoInfo == None:
            return False, "ID do Equipamento inválido!"

        return True, ""
    #Função para salvar a nova manutenção
    def salvarManutencao(self):
        dados_manutencao = self.obterDadosFormulario()

        result, message = self.verificarCamposObrigatorios(dados_manutencao)
        if not result:
            messagebox.showwarning("Falha ao Criar Nova Manutenção", message=message)
            return

        # Obter id unico da manutenção
        dados_manutencao["_id"] = ObjectId()
        
        # obter data e hora atuais
        dados_manutencao["data_inicio"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # salvar nova manutenção no banco de dados
        successo = self.manutencoesService.criarNovaManutencao(dados_manutencao)
        if not successo:
            messagebox.showerror("Erro ao Criar Nova Manutenção", "Não foi possível salvar a nova Manutenção no Banco de Dados")
        # resetar os campos do formulário  
        self.open_manutencoes_callback(dados_manutencao.get("id_equipamento")) # Abre a aba de manutenções com filtro pelo equipamento
        messagebox.showinfo("Criação de Nova Manutenção", "Nova Manutenção criada com Sucesso!") # Mensagem que a manutenção foi criada com sucesso
