# --- rural_controller.py ---

class RuralController:
    def __init__(self, app_controller):
        self.app_controller = app_controller

    def abrir_janela_cadastro(self):
        print("Funcionalidade de cadastro rural ainda não implementada.")
        self.app_controller.view.show_error("Não implementado", "A tela de cadastro para imóveis rurais ainda não foi criada.")

    def mostrar_tabelas_rurais(self):
        print("Funcionalidade de tabelas rurais ainda não implementada.")
        self.app_controller.view.show_error("Não implementado", "As tabelas para imóveis rurais ainda não foram criadas.")