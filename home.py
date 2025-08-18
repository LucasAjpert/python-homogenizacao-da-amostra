# --- home.py ---

from tkinter import *
from tkinter import messagebox
import model

# --- Configuração da Janela Principal ---
janela = Tk()
janela.title('Homogenização da Amostra')
janela.configure(bg="lightblue")
janela.geometry("300x350")

# --- DEFINIÇÃO DAS FONTES ---
fonte_padrao = ("Arial", 10)
fonte_botoes = ("Arial", 10, "bold")

# --- Frame para os Radio Buttons ---
frame_opcoes = Frame(janela, bg="lightblue")
frame_opcoes.pack(pady=10, padx=20, fill='x')

tipo_avaliacao = StringVar(value="urbano")

# 1. O Label fica no topo do frame principal de opções
label_tipo = Label(
    frame_opcoes, text="Informe o tipo de avaliação:",
    bg="lightblue", font=fonte_padrao
)
label_tipo.pack(anchor='w') # Alinhado à esquerda

# 2. Criamos um novo frame SÓ para os radio buttons
frame_radios = Frame(frame_opcoes, bg="lightblue")
frame_radios.pack(anchor='w') # Este frame fica abaixo do label

# 3. Colocamos os radio buttons dentro do novo frame, um ao lado do outro
radio_urbano = Radiobutton(
    frame_radios, # <-- Note que o pai agora é 'frame_radios'
    text="Urbano", variable=tipo_avaliacao,
    value="urbano", bg="lightblue", font=fonte_padrao
)
radio_urbano.pack(side=LEFT) # Empacotado à esquerda

radio_rurais = Radiobutton(
    frame_radios, # <-- O pai também é 'frame_radios'
    text="Imóveis Rurais", variable=tipo_avaliacao,
    value="rural", bg="lightblue", font=fonte_padrao
)
radio_rurais.pack(side=LEFT) # Empacotado à esquerda, ao lado do anterior


# --- Frame para os Botões Principais ---
frame_botoes = Frame(janela, bg="lightblue")
frame_botoes.pack(pady=10, padx=20, fill='x')

# --- Estilo para os botões padrão ---
estilo_botao = {
    "bg": "#007BFF",
    "fg": "white",
    "font": fonte_botoes,
    "relief": "raised",
    "borderwidth": 2,
    "width": 15
}

# --- Criação dos 5 Botões (estilo padrão) ---
btn_novo = Button(frame_botoes, text="Novo Calculo", command=model.novo_calculo, **estilo_botao)
btn_novo.pack(pady=4)

btn_visualizar = Button(frame_botoes, text="Visualizar", command=model.visualizar, **estilo_botao)
btn_visualizar.pack(pady=4)

btn_atualizar = Button(frame_botoes, text="Atualizar", command=model.atualizar, **estilo_botao)
btn_atualizar.pack(pady=4)

btn_delete = Button(frame_botoes, text="Delete", command=model.delete, **estilo_botao)
btn_delete.pack(pady=4)

btn_sair = Button(frame_botoes, text="Sair", command=lambda: model.sair(janela), **estilo_botao)
btn_sair.pack(pady=4)

# --- Inicia o loop da aplicação ---
janela.mainloop()