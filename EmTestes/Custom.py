
import tkinter as tk
from tkinter import ttk

MAIN_BACKGROUND_COLOR = "#252F60"
LATERAL_MENU_COLOR = "#353F6E"


class mainApp:

    def __init__(self, root):

        self.root = root
        self.root.title("GEMA")
        self.root.state("zoomed")  # Janela maximizada

        self.menuLateral = tk.Frame(self.root, width=250, bg=LATERAL_MENU_COLOR)
        self.menuLateral.pack(side="left", fill="y")

        self.areaPrincipal = tk.Frame(self.root, bg=MAIN_BACKGROUND_COLOR)
        self.areaPrincipal.pack(side="right", expand=True, fill="both")

        self.filtroFrame = tk.Frame(self.areaPrincipal, height=125, bg=MAIN_BACKGROUND_COLOR)
        self.filtroFrame.pack(side="top", fill="x")

        self.tabelaFrame = tk.Frame(self.areaPrincipal, bg=MAIN_BACKGROUND_COLOR)
        self.tabelaFrame.pack(side="bottom", expand=True, fill="both")

        #self.areaPrincipalTitle = tk.Label(self.areaPrincipal, text="Área Principal", bg="#252F60", fg="white", font=("Arial", 24))
        #self.areaPrincipalTitle.pack(pady=20)

        self.criarTabela()
        self.atualizarTabela([
            ("Dado 1", "Dado 2", "Dado 3", "Dado 4", "Dado 5"),
            ("Dado A", "Dado B", "Dado C", "Dado D", "Dado E"),
            ("Info 1", "Info 2", "Info 3", "Info 4", "Info 5")])

    def criarTabela(self):
        # Configure a style so the Treeview background matches the main area
        style = ttk.Style(self.root)
        # Use a simple theme so style changes are respected across platforms
        try:
            style.theme_use('default')
        except Exception:
            # keep default theme if 'default' not available
            pass

        style.configure("Custom.Treeview",
                        background=MAIN_BACKGROUND_COLOR,
                        fieldbackground=MAIN_BACKGROUND_COLOR,
                        foreground="white",
                        bordercolor=MAIN_BACKGROUND_COLOR,
                        borderwidth=0)
        style.configure("Custom.Treeview.Heading",
                        background=LATERAL_MENU_COLOR,
                        foreground="white")
        # selection color
        style.map("Custom.Treeview",
                  background=[('selected', '#46508A')],
                  foreground=[('selected', 'white')])

        # Exemplo de criação de tabela usando Treeview com estilo aplicado
        self.tabela = ttk.Treeview(self.tabelaFrame, columns=("col1", "col2", "col3", "col4", "col5"), show="headings", style="Custom.Treeview")
        self.tabela.heading("col1", text="Coluna 1")
        self.tabela.heading("col2", text="Coluna 2")
        self.tabela.heading("col3", text="Coluna 3")
        self.tabela.heading("col4", text="Coluna 4")
        self.tabela.heading("col5", text="Coluna 5")
        self.tabela.pack(expand=True, fill='both')

        # Configure tags so inserted rows use the same background color.
        # Keeping odd/even the same ensures a uniform look against the main background.
        self.tabela.tag_configure('odd', background=MAIN_BACKGROUND_COLOR, foreground='white')
        self.tabela.tag_configure('even', background=MAIN_BACKGROUND_COLOR, foreground='white')

    def atualizarTabela(self, dados):
        # Limpa a tabela existente
        for item in self.tabela.get_children():
            self.tabela.delete(item)
        # Adiciona novos dados à tabela
        for idx, linha in enumerate(dados):
            tag = 'odd' if (idx % 2) == 0 else 'even'
            self.tabela.insert("", tk.END, values=linha, tags=(tag,))


if __name__ == "__main__":
    root = tk.Tk()
    app = mainApp(root)
    root.mainloop()