import tkinter as tk
from tkinter import ttk

class AbaNovaManutencao:
    def __init__(self, areaPrincipal):

        self.mainFrame = tk.Frame(areaPrincipal, bg="#252F60")
        
        self.label = tk.Label(self.mainFrame, text="Aqui será a interface para criar uma nova manutenção", bg="#252F60", fg="white")
        self.label.pack(pady=20)

        # Campos do formulário para nova manutenção (criados manualmente para poder ajustar tamanhos)
        # ID Equipamento
        lbl_id = tk.Label(self.mainFrame, text="ID Equipamento", bg="#252F60", fg="white")
        lbl_id.pack(anchor="w", padx=20)

        ent_id = tk.Entry(self.mainFrame, width=20)
        ent_id.pack(fill="x", padx=20, pady=2)

        # Coleção Equipamento
        lbl_colecao = tk.Label(self.mainFrame, text="Coleção Equipamento", bg="#252F60", fg="white")
        lbl_colecao.pack(anchor="w", padx=20)

        ent_colecao = tk.Entry(self.mainFrame, width=30)
        ent_colecao.pack(fill="x", padx=20, pady=2)

        # Solicitante
        lbl_solicitante = tk.Label(self.mainFrame, text="Solicitante", bg="#252F60", fg="white")
        lbl_solicitante.pack(anchor="w", padx=20)

        ent_solicitante = tk.Entry(self.mainFrame, width=30)
        ent_solicitante.pack(fill="x", padx=20, pady=2)

        # Responsável
        lbl_responsavel = tk.Label(self.mainFrame, text="Responsável", bg="#252F60", fg="white")
        lbl_responsavel.pack(anchor="w", padx=20)

        ent_responsavel = tk.Entry(self.mainFrame, width=30)
        ent_responsavel.pack(fill="x", padx=20, pady=2)

        # Prioridade
        lbl_prioridade = tk.Label(self.mainFrame, text="Prioridade", bg="#252F60", fg="white")
        lbl_prioridade.pack(anchor="w", padx=20)

        cb_prioridade = ttk.Combobox(self.mainFrame, values=["Baixa", "Média", "Alta"], state="readonly", width=20)
        cb_prioridade.pack(fill="x", padx=20, pady=2)

        # Tipo
        lbl_tipo = tk.Label(self.mainFrame, text="Tipo", bg="#252F60", fg="white")
        lbl_tipo.pack(anchor="w", padx=20)

        cb_tipo = ttk.Combobox(self.mainFrame, values=["Corretiva", "Preventiva"], state="readonly", width=20)
        cb_tipo.pack(fill="x", padx=20, pady=2)

        # Descrição do Problema (campo maior — multi-linha)
        lbl_desc = tk.Label(self.mainFrame, text="Descrição do Problema", bg="#252F60", fg="white")
        lbl_desc.pack(anchor="w", padx=20)

        txt_desc = tk.Text(self.mainFrame, height=6, wrap="word")
        txt_desc.pack(fill="x", padx=20, pady=2)

        # Ação Realizada (pode ser multi-linha também)
        lbl_acao = tk.Label(self.mainFrame, text="Ação Realizada", bg="#252F60", fg="white")
        lbl_acao.pack(anchor="w", padx=20)

        txt_acao = tk.Text(self.mainFrame, height=4, wrap="word")
        txt_acao.pack(fill="x", padx=20, pady=2)

        # Data Início
        lbl_data_inicio = tk.Label(self.mainFrame, text="Data Início", bg="#252F60", fg="white")
        lbl_data_inicio.pack(anchor="w", padx=20)

        ent_data_inicio = tk.Entry(self.mainFrame, width=20)
        ent_data_inicio.pack(fill="x", padx=20, pady=2)

        # Data Conclusão
        lbl_data_fim = tk.Label(self.mainFrame, text="Data Conclusão", bg="#252F60", fg="white")
        lbl_data_fim.pack(anchor="w", padx=20)

        ent_data_fim = tk.Entry(self.mainFrame, width=20)
        ent_data_fim.pack(fill="x", padx=20, pady=2)

        # Status
        lbl_status = tk.Label(self.mainFrame, text="Status", bg="#252F60", fg="white")
        lbl_status.pack(anchor="w", padx=20)
        
        cb_status = ttk.Combobox(self.mainFrame, values=["Pendente", "Em andamento", "Concluída"], state="readonly", width=20)
        cb_status.pack(fill="x", padx=20, pady=2)

        # Armazena referências dos campos para uso posterior
        self.campos = {
            "ID Equipamento": ent_id,
            "Coleção Equipamento": ent_colecao,
            "Solicitante": ent_solicitante,
            "Responsável": ent_responsavel,
            "Prioridade": cb_prioridade,
            "Tipo": cb_tipo,
            "Descrição do Problema": txt_desc,
            "Ação Realizada": txt_acao,
            "Data Início": ent_data_inicio,
            "Data Conclusão": ent_data_fim,
            "Status": cb_status
        }

        # Botão para salvar
        self.btn_salvar = tk.Button(self.mainFrame, text="Salvar Manutenção", bg="#1E90FF", fg="white")
        self.btn_salvar.pack(pady=20)