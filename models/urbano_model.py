# --- models/urbano_model.py ---

from database import criar_conexao

class UrbanoModel:
    def add_imovel(self, dados_imovel):
        """Adiciona um novo imóvel urbano ao banco de dados."""
        conexao = criar_conexao()
        if conexao:
            cursor = conexao.cursor()
            # A ordem das colunas aqui deve corresponder à tabela do banco de dados
            sql = """
                INSERT INTO imoveis_urbanos (
                    endereco, area_construida, idade_imovel, valor_total, valor_unitario,
                    padrao_construtivo, valor_residual, conservacao_foc, indice_fiscal,
                    frentes_multiplas, idade_referencial, estado_conservacao, fator_oferta,
                    padao_const, conservacao, localizacao, frentes_m, unitario_homog,
                    benfeitorias, descricao_benfeitorias, tipo_cadastro
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            # A ordem dos valores aqui deve ser a mesma da query SQL
            valores = (
                dados_imovel.get('endereco'), dados_imovel.get('area_construida'), dados_imovel.get('idade_imovel'),
                dados_imovel.get('valor_total'), dados_imovel.get('valor_unitario'), dados_imovel.get('padrao_construtivo'),
                dados_imovel.get('valor_residual'), dados_imovel.get('conservacao_foc'), dados_imovel.get('indice_fiscal'),
                dados_imovel.get('frentes_multiplas'), dados_imovel.get('idade_referencial'), dados_imovel.get('estado_conservacao'),
                dados_imovel.get('fator_oferta'), dados_imovel.get('padao_const'), dados_imovel.get('conservacao'),
                dados_imovel.get('localizacao'), dados_imovel.get('frentes_m'), dados_imovel.get('unitario_homog'),
                dados_imovel.get('benfeitorias'), dados_imovel.get('descricao_benfeitorias'), dados_imovel.get('tipo_cadastro')
            )
            
            cursor.execute(sql, valores)
            conexao.commit()
            
            item_id = cursor.lastrowid # Pega o ID do item que acabamos de inserir
            
            cursor.close()
            conexao.close()
            print(f"Imóvel urbano com ID {item_id} adicionado ao banco de dados.")
            return item_id
        return None

    def get_todos_imoveis(self):
        """Busca todos os imóveis urbanos do banco de dados."""
        conexao = criar_conexao()
        if conexao:
            cursor = conexao.cursor(dictionary=True) # Retorna resultados como dicionários
            cursor.execute("SELECT * FROM imoveis_urbanos")
            imoveis = cursor.fetchall()
            cursor.close()
            conexao.close()
            return imoveis
        return []

    def update_imovel(self, item_id, novos_dados):
        """Atualiza os dados de um imóvel existente no banco de dados."""
        # Esta função precisará de uma query UPDATE...
        print(f"Lógica de UPDATE para o item {item_id} a ser implementada.")
        pass