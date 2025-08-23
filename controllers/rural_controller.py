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

    def mostrar_tabelas_rurais(self):
        print("Funcionalidade de tabelas rurais ainda não implementada.")
        messagebox.showinfo("Não implementado", "As tabelas para imóveis rurais ainda não foram criadas.")