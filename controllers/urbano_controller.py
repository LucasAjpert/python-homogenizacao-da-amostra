# --- controllers/urbano_controller.py ---

from models.urbano_model import UrbanoModel

class UrbanoController:
    def __init__(self, app_controller):
        self.app_controller = app_controller
        self.model = UrbanoModel()

    def salvar_dados(self, dados):
        """Recebe os dados da view e processa."""
        
        self.model.add_imovel(dados)
        print("Dados salvos no modelo:", dados)

        # A ordem das chaves aqui DEVE ser a mesma das colunas na View
        colunas_ids = [
            "endereco", "area_construida", "idade_imovel", "valor_total",
            "valor_unitario", "padrao_construtivo", "valor_residual",
            "conservacao_foc", "indice_fiscal", "frentes_multiplas",
            "idade_referencial", "estado_conservacao", "fator_oferta",
            "padao_const", "conservacao", "localizacao", "frentes_m",
            "unitario_homog"
        ]

        # Pega os valores na ordem correta, usando .get(chave, "") para evitar erros
        valores_para_treeview = tuple(dados.get(cid, "") for cid in colunas_ids)

        # Pede para a view (através do app_controller) para atualizar a tabela
        main_menu_frame = self.app_controller.view.get_frame("MainMenu")
        main_menu_frame.tree.insert("", "end", values=valores_para_treeview)