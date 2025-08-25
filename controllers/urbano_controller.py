# --- controllers/urbano_controller.py ---
from models.urbano_model import UrbanoModel
from calculos.calculos_urbanos import CalculosUrbanos

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
        """Recebe os dados da view, aplica as regras, calcula e processa."""
        
        main_menu_frame = self.app_controller.view.get_frame("MainMenu")
        tree = main_menu_frame.tree_urbano
        tipo_cadastro = dados.get('tipo_cadastro')
        
        # --- LÓGICA DE CÁLCULO Valor Total / Unitário ---
        try:
            area_str = dados.get('area_construida', '').replace(',', '.') or None
            total_str = dados.get('valor_total', '').replace(',', '.') or None
            unitario_str = dados.get('valor_unitario', '').replace(',', '.') or None
            area = float(area_str) if area_str else None
            total = float(total_str) if total_str else None
            unitario = float(unitario_str) if unitario_str else None
            if area is None or area == 0:
                self.app_controller.view.show_error("Erro de Validação", "O campo 'Área Construída' é obrigatório.")
                return
            if total is not None and unitario is not None:
                if abs((area * unitario) - total) > 0.01:
                    self.app_controller.view.show_error("Erro de Validação", "O Valor Total não corresponde ao cálculo.")
                    return
            elif unitario is not None and total is None:
                dados['valor_total'] = str(round(area * unitario, 2))
            elif total is not None and unitario is None:
                dados['valor_unitario'] = str(round(total / area, 2))
        except (ValueError, TypeError):
            self.app_controller.view.show_error("Erro de Formato", "Verifique se os campos de área e valores contêm apenas números válidos.")
            return
        
        # --- BUSCA OS DADOS DO IMÓVEL 'AVALIANDO' NA TREEVIEW ---
        padrao_avaliando = None
        foc_avaliando = None
        indice_fiscal_avaliando = None
        colunas_ids = self.get_colunas_ids()
        try:
            idx_padrao = colunas_ids.index('padrao_construtivo')
            idx_foc = colunas_ids.index('conservacao_foc')
            idx_if = colunas_ids.index('indice_fiscal') # Novo índice
            
            for item_id in tree.get_children():
                if 'avaliando_row' in tree.item(item_id, 'tags'):
                    valores_avaliando = tree.item(item_id, 'values')
                    padrao_avaliando = valores_avaliando[idx_padrao]
                    foc_avaliando = valores_avaliando[idx_foc]
                    indice_fiscal_avaliando = valores_avaliando[idx_if] # Pega o valor
                    break
        except ValueError as e:
            print(f"Erro: coluna não encontrada na Treeview - {e}")
            return

        if tipo_cadastro == 'amostra' and padrao_avaliando is None:
            self.app_controller.view.show_error("Erro de Validação", "É necessário cadastrar um imóvel 'Avaliando' primeiro.")
            return

        # --- EXECUTA OS CÁLCULOS (passando todos os dados do avaliando) ---
        calculadora = CalculosUrbanos(
            dados, 
            padrao_avaliando=padrao_avaliando, 
            foc_avaliando=foc_avaliando,
            indice_fiscal_avaliando=indice_fiscal_avaliando # Passa o novo valor
        )
        resultados_calculos = calculadora.executar_todos_os_calculos()
        dados.update(resultados_calculos)
        
        # --- LÓGICA DE VALIDAÇÃO E INSERÇÃO NA TREEVIEW ---
        if tipo_cadastro == 'avaliando':
            if padrao_avaliando is not None:
                self.app_controller.view.show_error("Erro de Validação", "Já existe um imóvel 'Avaliando'.")
                return

        valores_para_treeview = tuple(str(dados.get(cid, "")) for cid in colunas_ids)

        if tipo_cadastro == 'avaliando':
            tree.insert("", 0, values=valores_para_treeview, tags=('avaliando_row',))
        else:
            tree.insert("", "end", values=valores_para_treeview)
        
        self.model.add_imovel(dados)
        print("Dados salvos no modelo:", dados)

    def executar_atualizacao(self, novos_dados):
        """Salva os dados atualizados no modelo e na treeview."""
        if self.item_em_edicao_id:
            self.model.update_imovel(self.item_em_edicao_id, novos_dados)
            
            main_menu_frame = self.app_controller.view.get_frame("MainMenu")
            colunas_ids = self.get_colunas_ids()
            valores_atualizados = tuple(novos_dados.get(cid, "") for cid in colunas_ids)

            main_menu_frame.tree.item(self.item_em_edicao_id, values=valores_atualizados)
            
            self.item_em_edicao_id = None