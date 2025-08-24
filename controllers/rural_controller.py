# --- controllers/rural_controller.py ---

from tkinter import messagebox
from models.rural_model import RuralModel

class RuralController:
    def __init__(self, app_controller):
        self.app_controller = app_controller
        self.model = RuralModel()

    def salvar_dados(self, dados):
        """Recebe os dados do formulário rural e os processa."""
        print("--- DADOS DO IMÓVEL RURAL RECEBIDOS ---")
        
        # Pega a treeview rural da tela principal
        main_menu_frame = self.app_controller.view.get_frame("MainMenu")
        tree = main_menu_frame.tree_rural

        # Define a ordem correta das colunas
        colunas_rurais = main_menu_frame.colunas_rural
        
        # Pega os valores do dicionário de dados na ordem correta
        valores_para_treeview = tuple(dados.get(cid, "") for cid in colunas_rurais)

        # Insere na treeview
        tree.insert("", "end", values=valores_para_treeview)
        
        # No futuro, aqui também chamaremos a função para recalcular a média
        # self._atualizar_media()

