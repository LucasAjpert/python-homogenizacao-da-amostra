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
            self.show_frame("CadastroRural")

    def mostrar_tabelas(self):
        tipo = self.view.get_tipo_avaliacao()
        if tipo == "urbano":
            self.show_frame("TabelaUrbana")
        elif tipo == "rural":
            self.rural.mostrar_tabelas_rurais()

    def iniciar_atualizacao(self):
        """Pega o item selecionado e inicia o processo de atualização."""
        main_menu = self.view.get_frame("MainMenu")
        
        # Pega o ID do item selecionado na treeview
        item_selecionado = main_menu.tree.focus()
        
        if not item_selecionado:
            self.view.show_error("Erro de Seleção", "Por favor, selecione um item na tabela para atualizar.")
            return

        # Pega os valores do item selecionado
        dados_item_tupla = main_menu.tree.item(item_selecionado, 'values')
        
        tipo = self.view.get_tipo_avaliacao()
        if tipo == "urbano":
            self.urbano.abrir_janela_atualizacao(item_selecionado, dados_item_tupla)
        elif tipo == "rural":
            pass # Lógica futura

    def deletar_dados(self):
        print("Botão 'Delete' clicado")

    def sair(self):
        if messagebox.askokcancel("Sair", "Você tem certeza que quer sair?"):
            self.view.root.destroy()