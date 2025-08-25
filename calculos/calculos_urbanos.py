class CalculosUrbanos:
    def __init__(self, dados_imovel, padrao_avaliando=None, foc_avaliando=None, indice_fiscal_avaliando=None):
        self.dados = dados_imovel
        self.padrao_avaliando = padrao_avaliando
        self.foc_avaliando = foc_avaliando
        self.indice_fiscal_avaliando = indice_fiscal_avaliando
        self.resultados = {}

    def executar_todos_os_calculos(self):
        """
        Executa todos os cálculos em sequência e retorna os resultados.
        """
        # 1. Calcula todos os fatores individuais primeiro
        self.resultados['padao_const'] = self._calcular_padao_const()
        self.resultados['localizacao'] = self._calcular_localizacao()
        self.resultados['frentes_m'] = self._calcular_frentes_m()
        self.resultados['fator_oferta'] = self._calcular_fator_oferta()
        k = self._calcular_k()
        if k is not None:
            foc_amostra = self._calcular_conservacao_foc(k)
            self.resultados['conservacao_foc'] = foc_amostra
            self.resultados['conservacao'] = self._calcular_conservacao(foc_amostra)
        
        # 2. Por último, calcula o 'unitario_homog' que depende dos outros
        self.resultados['unitario_homog'] = self._calcular_unitario_homog()

        # Filtra chaves com valor None para não limpar campos preenchidos
        resultados_validos = {k: v for k, v in self.resultados.items() if v is not None}
        return resultados_validos

    def _calcular_unitario_homog(self):
        """
        Calcula o valor unitário homogeneizado da amostra.
        Fórmula: produto de todos os outros fatores calculados.
        """
        # Este cálculo só se aplica a imóveis 'Amostra'
        if self.dados.get('tipo_cadastro') != 'amostra':
            return "" # Deixa o campo vazio para o 'Avaliando'
        
        try:
            # Pega os valores já calculados e armazenados em self.resultados
            fator_oferta = float(self.resultados.get('fator_oferta', 1.0))
            padao_const = float(self.resultados.get('padao_const', 1.0))
            conservacao = float(self.resultados.get('conservacao', 1.0))
            localizacao = float(self.resultados.get('localizacao', 1.0))
            frentes_m = float(self.resultados.get('frentes_m', 1.0))

            resultado = fator_oferta * padao_const * conservacao * localizacao * frentes_m
            
            return round(resultado, 4)

        except (ValueError, TypeError) as e:
            print(f"Erro ao calcular Unitário Homogeneizado: {e}.")
            return None

    def _calcular_frentes_m(self):
        frentes_multiplas = self.dados.get('frentes_multiplas')
        if frentes_multiplas == 'Sim':
            return 0.9
        elif frentes_multiplas == 'Não':
            return 1.0
        else:
            return 1.0

    def _calcular_localizacao(self):
        if self.dados.get('tipo_cadastro') != 'amostra': return ""
        try:
            if_avaliando = float(str(self.indice_fiscal_avaliando or '0').replace(',', '.'))
            if_amostra = float(self.dados.get('indice_fiscal', '0').replace(',', '.'))
            if if_amostra == 0: return None
            return round(if_avaliando / if_amostra, 4)
        except (ValueError, TypeError): return None

    def _calcular_conservacao(self, foc_amostra):
        if self.dados.get('tipo_cadastro') != 'amostra': return ""
        try:
            foc_avaliando = float(str(self.foc_avaliando or '0').replace(',', '.'))
            if foc_amostra is None or foc_amostra == 0: return None
            return round(foc_avaliando / foc_amostra, 4)
        except (ValueError, TypeError): return None

    def _calcular_padao_const(self):
        if self.dados.get('tipo_cadastro') != 'amostra': return ""
        try:
            padrao_avaliando = float(str(self.padrao_avaliando or '0').replace(',', '.'))
            padrao_amostra = float(self.dados.get('padrao_construtivo', '0').replace(',', '.'))
            if padrao_amostra == 0 or padrao_avaliando == 0: return None
            return round(padrao_avaliando / padrao_amostra, 4)
        except (ValueError, TypeError): return None
    
    def _calcular_fator_oferta(self):
        try:
            valor_unitario = float(self.dados.get('valor_unitario', '0').replace(',', '.'))
            if valor_unitario > 0:
                return round(valor_unitario * 0.9, 2)
            return None
        except (ValueError, TypeError): return None

    def _calcular_conservacao_foc(self, k):
        try:
            valor_residual_input = float(self.dados.get('valor_residual', '0').replace(',', '.'))
            valor_residual = valor_residual_input / 100.0
            return round(valor_residual + (k * (1 - valor_residual)), 4)
        except (ValueError, TypeError): return None

    def _calcular_k(self):
        try:
            estado_conservacao_input = float(self.dados.get('estado_conservacao', '0').replace(',', '.'))
            idade_imovel = float(self.dados.get('idade_imovel', '0').replace(',', '.'))
            idade_referencial = float(self.dados.get('idade_referencial', '0').replace(',', '.'))
            if idade_referencial == 0: return None
            estado_conservacao = estado_conservacao_input / 100.0
            ratio = idade_imovel / idade_referencial
            depreciacao_idade = (ratio + ratio**2) / 2
            return round((1 - estado_conservacao) * (1 - depreciacao_idade), 4)
        except (ValueError, TypeError): return None