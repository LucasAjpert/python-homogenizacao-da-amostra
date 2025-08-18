# --- controllers/urbano_controller.py ---

from models.urbano_model import UrbanoModel

class UrbanoController:
    def __init__(self, app_controller):
        self.app_controller = app_controller
        self.model = UrbanoModel()

    def salvar_dados(self, dados):
        """Recebe os dados da view e processa."""
        
        # Pega apenas os dados que a Treeview espera
        dados_para_treeview = {
            "endereco": dados.get("endereco", ""),
            "area": dados.get("area_construida", ""),
            "idade": dados.get("idade_imovel", ""),
            "valor_unitario": dados.get("valor_unitario", "")
        }
        
        self.model.add_imovel(dados) # Salva todos os dados no modelo
        print("Dados salvos no modelo:", dados)

        # Pede para a view (através do app_controller) para atualizar a tabela
        main_menu_frame = self.app_controller.view.get_frame("MainMenu")
        main_menu_frame.tree.insert("", "end", values=(
            dados_para_treeview["endereco"],
            dados_para_treeview["area"],
            dados_para_treeview["idade"],
            dados_para_treeview["valor_unitario"]
        ))