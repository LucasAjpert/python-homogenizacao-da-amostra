# --- model.py ---

from tkinter import *
from tkinter import messagebox

def novo_calculo(tipo_avaliacao):
    """Lógica para iniciar um novo cálculo."""
    if tipo_avaliacao == "urbano":
        janela_cadastro = Toplevel()
        janela_cadastro.title("Cadastro de Imóvel Urbano")
        janela_cadastro.geometry("300x550")
        janela_cadastro.configure(bg="lightblue")

        # --- Frame Principal ---
        frame_principal = Frame(janela_cadastro, bg="lightblue", padx=10, pady=10)
        frame_principal.pack(fill='both', expand=True)

        # --- Widgets ---
        # Tipo de Cadastro (Avaliando/Amostra)
        tipo_cadastro = StringVar(value="avaliando")
        frame_tipo_cadastro = Frame(frame_principal, bg="lightblue")
        Label(frame_tipo_cadastro, text="Tipo de Cadastro:", bg="lightblue").pack(side=LEFT, padx=5)
        Radiobutton(frame_tipo_cadastro, text="Avaliando", variable=tipo_cadastro, value="avaliando", bg="lightblue").pack(side=LEFT)
        Radiobutton(frame_tipo_cadastro, text="Amostra", variable=tipo_cadastro, value="amostra", bg="lightblue").pack(side=LEFT)
        frame_tipo_cadastro.grid(row=0, column=0, columnspan=2, sticky='w', pady=5)

        # Endereço
        Label(frame_principal, text="Endereço:", bg="lightblue").grid(row=1, column=0, sticky='w', pady=2)
        Entry(frame_principal, width=20).grid(row=1, column=1, sticky='w', pady=2)

        # Área Construida
        Label(frame_principal, text="Área Construida:", bg="lightblue").grid(row=2, column=0, sticky='w', pady=2)
        Entry(frame_principal).grid(row=2, column=1, sticky='w', pady=2)

        # Idade do Imóvel
        Label(frame_principal, text="Idade do Imóvel:", bg="lightblue").grid(row=3, column=0, sticky='w', pady=2)
        Entry(frame_principal).grid(row=3, column=1, sticky='w', pady=2)

        # Valor Total
        Label(frame_principal, text="Valor Total:", bg="lightblue").grid(row=4, column=0, sticky='w', pady=2)
        Entry(frame_principal).grid(row=4, column=1, sticky='w', pady=2)

        # Valor Unitário
        Label(frame_principal, text="Valor Unitário:", bg="lightblue").grid(row=5, column=0, sticky='w', pady=2)
        Entry(frame_principal).grid(row=5, column=1, sticky='w', pady=2)

        # Padrão Construtivo
        Label(frame_principal, text="Padrão Construtivo:", bg="lightblue").grid(row=6, column=0, sticky='w', pady=2)
        Entry(frame_principal).grid(row=6, column=1, sticky='w', pady=2)

        # Valor Residual
        Label(frame_principal, text="Valor Residual (ex: 20):", bg="lightblue").grid(row=7, column=0, sticky='w', pady=2)
        Entry(frame_principal).grid(row=7, column=1, sticky='w', pady=2)

        # *Conservação Foc
        Label(frame_principal, text="*Conservação Foc:", bg="lightblue").grid(row=8, column=0, sticky='w', pady=2)
        Entry(frame_principal).grid(row=8, column=1, sticky='w', pady=2)

        # Indice Fiscal
        Label(frame_principal, text="Indice Fiscal:", bg="lightblue").grid(row=9, column=0, sticky='w', pady=2)
        Entry(frame_principal).grid(row=9, column=1, sticky='w', pady=2)

        # Frentes Múltiplas
        frentes_multiplas = StringVar(value="Não")
        frame_frentes = Frame(frame_principal, bg="lightblue")
        Label(frame_frentes, text="Frentes Múltiplas:", bg="lightblue").pack(side=LEFT, padx=5)
        Radiobutton(frame_frentes, text="Sim", variable=frentes_multiplas, value="Sim", bg="lightblue").pack(side=LEFT)
        Radiobutton(frame_frentes, text="Não", variable=frentes_multiplas, value="Não", bg="lightblue").pack(side=LEFT)
        frame_frentes.grid(row=10, column=0, columnspan=2, sticky='w', pady=5)

        # Idade Referencial em anos
        Label(frame_principal, text="Idade Referencial em anos:", bg="lightblue").grid(row=11, column=0, sticky='w', pady=2)
        Entry(frame_principal).grid(row=11, column=1, sticky='w', pady=2)

        # Estado de Conservação - EC
        Label(frame_principal, text="Estado de Conservação - EC:", bg="lightblue").grid(row=12, column=0, sticky='w', pady=2)
        Entry(frame_principal).grid(row=12, column=1, sticky='w', pady=2)

        # *Fator Oferta
        Label(frame_principal, text="*Fator Oferta:", bg="lightblue").grid(row=13, column=0, sticky='w', pady=2)
        Entry(frame_principal).grid(row=13, column=1, sticky='w', pady=2)

        # *Padão Const.
        Label(frame_principal, text="*Padão Const.:", bg="lightblue").grid(row=14, column=0, sticky='w', pady=2)
        Entry(frame_principal).grid(row=14, column=1, sticky='w', pady=2)

        # *Conservação
        Label(frame_principal, text="*Conservação:", bg="lightblue").grid(row=15, column=0, sticky='w', pady=2)
        Entry(frame_principal).grid(row=15, column=1, sticky='w', pady=2)
        
        # *Localização
        Label(frame_principal, text="*Localização:", bg="lightblue").grid(row=16, column=0, sticky='w', pady=2)
        Entry(frame_principal).grid(row=16, column=1, sticky='w', pady=2)
        
        # *Frentes M
        Label(frame_principal, text="*Frentes M:", bg="lightblue").grid(row=17, column=0, sticky='w', pady=2)
        Entry(frame_principal).grid(row=17, column=1, sticky='w', pady=2)
        
        # *Unitário Homog.
        Label(frame_principal, text="*Unitário Homog.:", bg="lightblue").grid(row=18, column=0, sticky='w', pady=2)
        Entry(frame_principal).grid(row=18, column=1, sticky='w', pady=2)

        # Botão para salvar
        Button(frame_principal, text="Salvar", command=lambda: print("Dados salvos!")).grid(row=19, column=0, columnspan=2, pady=10)


    else:
        print("Botão 'Novo Calculo' clicado para Imóveis Rurais")


def tabelas():
    """Lógica para visualizar as tabelas."""
    print("Botão 'Tabelas' clicado")

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