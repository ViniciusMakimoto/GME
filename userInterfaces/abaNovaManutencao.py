import tkinter as tk
from tkinter import ttk

from services.novaManutencaoService import NovaManutencaoService

class AbaNovaManutencao:
    def __init__(self, areaPrincipal):

        self.mainFrame = tk.Frame(areaPrincipal, bg="#252F60")
        
        # Ajusta o grid para expandir os campos corretamente
        self.mainFrame.columnconfigure(0, weight=0)
        self.mainFrame.columnconfigure(1, weight=1)
        self.mainFrame.columnconfigure(2, weight=1)
        self.mainFrame.columnconfigure(3, weight=2)

        self.label = tk.Label(self.mainFrame, text="Registar Nova Manutenção", font=("Arial", 20), bg="#252F60", fg="white")
        self.label.grid(row=0, column=0, columnspan=4, pady=20, sticky="ew")

        self.initGUI()
        self.novaManutencaoService = NovaManutencaoService()

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
        self.btn_salvar = tk.Button(self.mainFrame, text="Salvar Manutenção", bg="#1E90FF", fg="white")
        self.btn_salvar.grid(row=7, column=1, columnspan=3, sticky="ew", padx=5, pady=2)

        # Armazena referências dos campos para uso posterior
        self.campos = {
            "ID Equipamento": ent_id,
            "Solicitante": ent_solicitante,
            "Prioridade": cb_prioridade,
            "Tipo": cb_tipo,
            "Descrição do Problema": txt_desc,
            "Status": cb_status
        }
    
    def resetOptions(self):
        for _, widget in self.campos.items():
            if isinstance(widget, tk.Entry):
                widget.delete(0, tk.END)
            elif isinstance(widget, tk.Text):
                widget.delete("1.0", tk.END)
            elif isinstance(widget, ttk.Combobox):
                widget.current(0)

    def obterDadosFormulario(self):
        dados = {}
        for chave, widget in self.campos.items():
            if isinstance(widget, tk.Entry):
                dados[chave] = widget.get().strip()
            elif isinstance(widget, ttk.Combobox):
                dados[chave] = widget.get().strip()
            elif isinstance(widget, tk.Text):
                dados[chave] = widget.get("1.0", tk.END).strip()
        return dados