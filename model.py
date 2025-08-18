# --- model.py ---

from tkinter import messagebox

def novo_calculo():
    """Lógica para iniciar um novo cálculo."""
    print("Botão 'Novo Calculo' clicado")

def visualizar():
    """Lógica para visualizar cálculos existentes."""
    print("Botão 'Visualizar' clicado")

def atualizar():
    """Lógica para atualizar um cálculo."""
    print("Botão 'Atualizar' clicado")

def delete():
    """Lógica para deletar um cálculo."""
    print("Botão 'Delete' clicado")

def sair(janela_principal):
    """Fecha a aplicação após confirmação."""
    if messagebox.askokcancel("Sair", "Você tem certeza que quer sair?"):
        janela_principal.destroy()