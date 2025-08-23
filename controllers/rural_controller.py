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
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")
        
        # No futuro, aqui entrará a lógica para salvar no modelo
        # e para adicionar na treeview de imóveis rurais.
        # self.model.add_imovel(dados)

