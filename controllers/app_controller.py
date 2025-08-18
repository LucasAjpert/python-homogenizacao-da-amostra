# --- controllers/app_controller.py ---

from .urbano_controller import UrbanoController
from .rural_controller import RuralController
from tkinter import messagebox

class AppController:
    def __init__(self):
        self.view = None
        # Passa a si mesmo (o app_controller) para os sub-controllers
        self.urbano = UrbanoController(self)
        self.rural = RuralController(self)

    def set_view(self, view):
        self.view = view

    def show_frame(self, page_name):
        self.view.show_frame(page_name)

    def iniciar_novo_calculo(self):
        tipo = self.view.get_tipo_avaliacao()
        if tipo == "urbano":
            self.show_frame("CadastroUrbano")
        elif tipo == "rural":
            self.rural.abrir_janela_cadastro()

    def mostrar_tabelas(self):
        tipo = self.view.get_tipo_avaliacao()
        if tipo == "urbano":
            self.show_frame("TabelaUrbana")
        elif tipo == "rural":
            self.rural.mostrar_tabelas_rurais()

    def atualizar_dados(self, event=None):
        print("Botão 'Atualizar' ou F5 pressionado")

    def deletar_dados(self):
        print("Botão 'Delete' clicado")

    def sair(self):
        if messagebox.askokcancel("Sair", "Você tem certeza que quer sair?"):
            self.view.root.destroy()