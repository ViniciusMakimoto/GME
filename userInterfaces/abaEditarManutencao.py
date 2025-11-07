import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

from services.manutencoesService import ManutencoesService
from services.equipamentosService import EquipamentosService
from bson import ObjectId

STATUS_OPTIONS = ["Pendente", "Em Andamento", "Concluído", "Cancelado"]

class AbaEditarManutencao:
    def __init__(self, areaPrincipal, open_manutencoes_callback):

        self.mainFrame = tk.Frame(areaPrincipal, bg="#252F60")
        
        # Ajusta o grid para expandir os campos corretamente
        self.mainFrame.columnconfigure(0, weight=0)
        self.mainFrame.columnconfigure(1, weight=1)
        self.mainFrame.columnconfigure(2, weight=1)
        self.mainFrame.columnconfigure(3, weight=2)

        self.label = tk.Label(self.mainFrame, text="Editar Nova Manutenção", font=("Arial", 20), bg="#252F60", fg="white")
        self.label.grid(row=0, column=0, columnspan=4, pady=20, sticky="ew")

        self.initGUI() #Inicializa os componentes da GUI
        self.manutencoesService = ManutencoesService() #instancia o serviço de manutenções
        self.equipamentoService = EquipamentosService() #instancia o serviço de equipamentos
        self.open_manutencoes_callback = open_manutencoes_callback #Callback para abrir a aba de manutenções

    def initGUI(self):
        # ID Manutenção
        lbl_id_manutencao = tk.Label(self.mainFrame, text="ID Manutenção", bg="#252F60", fg="white")
        lbl_id_manutencao.grid(row=1, column=0, sticky="w", padx=20, pady=2)

        ent_id_manutencao = tk.Entry(self.mainFrame, width=18, state="disabled")
        ent_id_manutencao.grid(row=1, column=1, sticky="ew", padx=5, pady=2)

        # ID Equipamento
        lbl_id = tk.Label(self.mainFrame, text="ID Equipamento", bg="#252F60", fg="white")
        lbl_id.grid(row=2, column=0, sticky="w", padx=20, pady=2)

        ent_id = tk.Entry(self.mainFrame, width=18, state="disabled")
        ent_id.grid(row=2, column=1, sticky="ew", padx=5, pady=2)

        # Solicitante
        lbl_solicitante = tk.Label(self.mainFrame, text="Solicitante", bg="#252F60", fg="white")
        lbl_solicitante.grid(row=3, column=0, sticky="w", padx=20, pady=2)

        ent_solicitante = ttk.Combobox(self.mainFrame, values=["Ryan", "Pedro"], width=12)
        ent_solicitante.grid(row=3, column=1, sticky="ew", padx=5, pady=2)

        # Responsável
        lbl_responsavel = tk.Label(self.mainFrame, text="Responsável", bg="#252F60", fg="white")
        lbl_responsavel.grid(row=4, column=0, sticky="w", padx=20, pady=2)

        ent_responsavel = ttk.Combobox(self.mainFrame, values=["Ryan", "Pedro"], width=12)
        ent_responsavel.grid(row=4, column=1, sticky="ew", padx=5, pady=2)

        # Status (combo menor)
        lbl_status = tk.Label(self.mainFrame, text="Status", bg="#252F60", fg="white")
        lbl_status.grid(row=5, column=0, sticky="w", padx=20, pady=2)

        cb_status = ttk.Combobox(self.mainFrame, values=STATUS_OPTIONS, state="readonly", width=12)
        cb_status.grid(row=5, column=1, sticky="ew", padx=5, pady=2)

        # Prioridade (combo menor)
        lbl_prioridade = tk.Label(self.mainFrame, text="Prioridade", bg="#252F60", fg="white")
        lbl_prioridade.grid(row=6, column=0, sticky="w", padx=20, pady=2)

        cb_prioridade = ttk.Combobox(self.mainFrame, values=["Baixa", "Média", "Alta"], state="readonly", width=12)
        cb_prioridade.grid(row=6, column=1, sticky="ew", padx=5, pady=2)

        # Tipo (combo menor)
        lbl_tipo = tk.Label(self.mainFrame, text="Tipo", bg="#252F60", fg="white")
        lbl_tipo.grid(row=7, column=0, sticky="w", padx=20, pady=2)

        cb_tipo = ttk.Combobox(self.mainFrame, values=["Corretiva", "Preventiva"], state="readonly", width=12)
        cb_tipo.grid(row=7, column=1, sticky="ew", padx=5, pady=2)

        # Descrição do Problema (campo maior — multi-linha)
        lbl_desc = tk.Label(self.mainFrame, text="Descrição do Problema", bg="#252F60", fg="white")
        lbl_desc.grid(row=8, column=0, sticky="nw", padx=20, pady=2)

        txt_desc = tk.Text(self.mainFrame, height=5, wrap="word")
        txt_desc.grid(row=8, column=1, columnspan=3, sticky="ew", padx=5, pady=2)

        # Ação Realizada (campo maior — multi-linha)
        lbl_acao = tk.Label(self.mainFrame, text="Ação Realizada", bg="#252F60", fg="white")
        lbl_acao.grid(row=9, column=0, sticky="nw", padx=20, pady=2)

        txt_acao = tk.Text(self.mainFrame, height=5, wrap="word")
        txt_acao.grid(row=9, column=1, columnspan=3, sticky="ew", padx=5, pady=2)

        # Botão para salvar
        self.btn_salvar = tk.Button(self.mainFrame, text="Salvar Alterações", bg="#1E90FF", fg="white", command=self.salvarAlteracao)
        self.btn_salvar.grid(row=10, column=1, columnspan=3, sticky="ew", padx=5, pady=2)

        # Armazena referências dos campos para uso posterior
        self.campos = {
            "_id": ent_id_manutencao,
            "id_equipamento": ent_id,
            "solicitante": ent_solicitante,
            "responsável": ent_responsavel,
            "prioridade": cb_prioridade,
            "tipo": cb_tipo,
            "descricao_problema": txt_desc,
            "acao_realizada": txt_acao,
            "status": cb_status
        }
    #verifica se a manutenção com o ID fornecido é válida
    def verificarManutencaoValida(self, manutecao_id):
        manutencaoInfo = self.manutencoesService.obterManutencaoPorID(ObjectId(manutecao_id))
        if manutencaoInfo == None:
            messagebox.showwarning("Erro ao Editar Manutenção", "Não foi possível editar Manutenção - ID Inválido")
            return False

        return True
    #obtém os dados atuais da manutenção a partir do serviço de manutenções  
    def obterDadosAtuais(self, manutecao_id):
        return self.manutencoesService.obterManutencaoPorID(ObjectId(manutecao_id))
    #popula os campos do formulário com os dados da manutenção
    def popularCampos(self, manutecao_id):
        dados = self.obterDadosAtuais(manutecao_id)

        for chave, widget in self.campos.items():
            if chave in dados:
                valor = dados[chave]
            else:
                valor = ""
                
            if isinstance(widget, ttk.Combobox):
                widget.set(valor)
            elif isinstance(widget, tk.Entry):
                lastState = widget.cget('state')
                widget.config(state="normal")
                widget.delete(0, tk.END)
                widget.insert(0, str(valor))
                widget.config(state=lastState)
            elif isinstance(widget, tk.Text):
                widget.delete("1.0", tk.END)
                widget.insert(tk.END, str(valor))
    
    def obterDadosFormulario(self):
        dados = {}
        for chave, widget in self.campos.items():
            if isinstance(widget, ttk.Combobox):
                dados[chave] = widget.get().strip()
            elif isinstance(widget, tk.Entry):
                dados[chave] = widget.get().strip()
            elif isinstance(widget, tk.Text):
                dados[chave] = widget.get("1.0", tk.END).strip()
        return dados
    
    def verificarCamposObrigatorios(self, dados):
        campos_obrigatorios = ["id_equipamento", "solicitante", "descricao_problema"]
        for campo in campos_obrigatorios: 
            if not dados.get(campo): #verifica se o campo está vazio
                return False, f"Campo {campo} não pode ser vazio!"
            
        ID_Equipamento = int(dados.get("id_equipamento"))
            
        equipamentoInfo = self.equipamentoService.obterEquipamentoPorID(ID_Equipamento)
        if equipamentoInfo == None:
            return False, "ID do Equipamento inválido!"

        return True, ""
    
    def salvarAlteracao(self):
        dados_manutencao = self.obterDadosFormulario()

        result, message = self.verificarCamposObrigatorios(dados_manutencao)
        if not result:
            messagebox.showwarning("Falha ao Editar Nova Manutenção", message=message)
            return
        
        # obter data e hora atuais
        dados_manutencao["data_conclusao"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        ID = ObjectId(dados_manutencao["_id"])

        if '_id' in dados_manutencao:
            del dados_manutencao['_id']

        successo = self.manutencoesService.atualizarManutencaoPorID(ID, dados_manutencao)
        if not successo:
            messagebox.showerror("Erro ao Editar Manutenção", "Não foi possível editar a Manutenção no Banco de Dados")
        
        self.open_manutencoes_callback(dados_manutencao.get("id_equipamento"))
        messagebox.showinfo("Editar Manutenção", "Manutenção editada com Sucesso!")
