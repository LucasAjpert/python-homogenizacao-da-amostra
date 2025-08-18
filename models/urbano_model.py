# --- urbano_model.py ---

class UrbanoModel:
    def __init__(self):
        self.imoveis_cadastrados = []

    def add_imovel(self, dados_imovel):
        # Aqui você poderia adicionar validações ou salvar em um banco de dados
        self.imoveis_cadastrados.append(dados_imovel)
        print("Imóvel urbano adicionado ao modelo:", dados_imovel)

    def get_todos_imoveis(self):
        return self.imoveis_cadastrados