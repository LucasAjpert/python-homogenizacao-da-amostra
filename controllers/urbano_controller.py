# --- controllers/urbano_controller.py ---

from models.urbano_model import UrbanoModel

class UrbanoController:
    def __init__(self, app_controller):
        self.app_controller = app_controller
        self.model = UrbanoModel()
        self.item_em_edicao_id = None

    def get_colunas_ids(self):
        """Helper para manter a lista de colunas em um só lugar."""
        return [
            "endereco", "area_construida", "idade_imovel", "valor_total",
            "valor_unitario", "padrao_construtivo", "valor_residual",
            "conservacao_foc", "indice_fiscal", "frentes_multiplas",
            "idade_referencial", "estado_conservacao", "fator_oferta",
            "padao_const", "conservacao", "localizacao", "frentes_m",
            "unitario_homog", "benfeitorias" # <-- NOVO CAMPO ADICIONADO
        ]

    def salvar_dados(self, dados):
        """Recebe os dados da view e processa."""
        main_menu_frame = self.app_controller.view.get_frame("MainMenu")
        
        colunas_ids = self.get_colunas_ids()
        valores_para_treeview = tuple(dados.get(cid, "") for cid in colunas_ids)
        
        item_id = main_menu_frame.tree.insert("", "end", values=valores_para_treeview)
        self.model.add_imovel(item_id, dados)
        print("Dados salvos no modelo:", dados)

    def abrir_janela_atualizacao(self, item_id, dados_tupla):
        """Abre a tela de edição e preenche com os dados do item."""
        self.item_em_edicao_id = item_id
        
        colunas_ids = self.get_colunas_ids()
        dados_dict = dict(zip(colunas_ids, dados_tupla))

        frame_atualizacao = self.app_controller.view.get_frame("AtualizacaoUrbana")
        frame_atualizacao.popular_formulario(dados_dict)
        
        self.app_controller.show_frame("AtualizacaoUrbana")

    def executar_atualizacao(self, novos_dados):
        """Salva os dados atualizados no modelo e na treeview."""
        if self.item_em_edicao_id:
            self.model.update_imovel(self.item_em_edicao_id, novos_dados)
            
            main_menu_frame = self.app_controller.view.get_frame("MainMenu")
            colunas_ids = self.get_colunas_ids()
            valores_atualizados = tuple(novos_dados.get(cid, "") for cid in colunas_ids)

            main_menu_frame.tree.item(self.item_em_edicao_id, values=valores_atualizados)
            
            self.item_em_edicao_id = None