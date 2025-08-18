# --- view.py ---

import os
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class MainView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title('Homogenização da Amostra')
        self.root.geometry("800x600")
        self.root.configure(bg="lightblue")

        self.fonte_padrao = ("Arial", 10)
        self.fonte_botoes = ("Arial", 10, "bold")
        self.tipo_avaliacao = StringVar(value="urbano")

        container = Frame(root)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainMenu, TabelaUrbana, CadastroUrbano):
            page_name = F.__name__
            # --- CORREÇÃO AQUI: Passa a própria instância da MainView (self) para os frames ---
            frame = F(parent=container, controller=self.controller, view=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        if hasattr(frame, 'on_show'):
            frame.on_show()
        frame.tkraise()

    def get_frame(self, page_name):
        return self.frames[page_name]
        
    def get_tipo_avaliacao(self):
        return self.tipo_avaliacao.get()

# =============================================================================
# --- TELA: MENU PRINCIPAL ---
# =============================================================================
class MainMenu(Frame):
    # --- CORREÇÃO AQUI: Recebe a 'view' como argumento ---
    def __init__(self, parent, controller, view):
        super().__init__(parent, bg="lightblue")
        self.controller = controller
        self.view = view # Armazena a referência da view principal

        frame_opcoes = Frame(self, bg="lightblue")
        frame_opcoes.pack(pady=10, padx=20, fill='x', expand=True)
        Label(frame_opcoes, text="Informe o tipo de avaliação:", bg="lightblue").pack(anchor='center')
        frame_radios = Frame(frame_opcoes, bg="lightblue")
        frame_radios.pack(anchor='center')
        
        # --- CORREÇÃO AQUI: Usa a referência direta da 'view' que foi passada ---
        Radiobutton(frame_radios, text="Urbano", variable=self.view.tipo_avaliacao, value="urbano", bg="lightblue").pack(side=LEFT)
        Radiobutton(frame_radios, text="Imóveis Rurais", variable=self.view.tipo_avaliacao, value="rural", bg="lightblue").pack(side=LEFT)
        
        frame_botoes = Frame(self, bg="lightblue")
        frame_botoes.pack(pady=5, padx=20, fill='x', expand=True)
        estilo_botao = {"bg": "#007BFF", "fg": "white", "font": ("Arial", 10, "bold"), "relief": "raised", "borderwidth": 2, "width": 15}
        Button(frame_botoes, text="Novo Calculo", command=self.controller.iniciar_novo_calculo, **estilo_botao).pack(pady=4)
        Button(frame_botoes, text="Tabelas", command=self.controller.mostrar_tabelas, **estilo_botao).pack(pady=4)
        Button(frame_botoes, text="Atualizar", command=self.controller.atualizar_dados, **estilo_botao).pack(pady=4)
        Button(frame_botoes, text="Delete", command=self.controller.deletar_dados, **estilo_botao).pack(pady=4)
        Button(frame_botoes, text="Sair", command=self.controller.sair, **estilo_botao).pack(pady=4)
        
        frame_treeview = Frame(self, bg="lightblue")
        frame_treeview.pack(pady=10, padx=10, fill='both', expand=True)
        colunas = ("endereco", "area", "idade", "valor_unitario")
        self.tree = ttk.Treeview(frame_treeview, columns=colunas, show='headings')
        self.tree.heading("endereco", text="Endereço")
        self.tree.heading("area", text="Área Construída")
        self.tree.heading("idade", text="Idade do Imóvel")
        self.tree.heading("valor_unitario", text="Valor Unitário")
        self.tree.pack(fill='both', expand=True)

# =============================================================================
# --- TELA: TABELA URBANA (IMAGENS) ---
# =============================================================================
class TabelaUrbana(Frame):
    def __init__(self, parent, controller, view):
        super().__init__(parent, bg="lightblue")
        self.controller = controller
        self.view = view
        self.imagens_carregadas = False

    def on_show(self):
        if not self.imagens_carregadas:
            self.carregar_conteudo()
            self.imagens_carregadas = True

    def carregar_conteudo(self):
        Label(self, text="Tabelas de Referência (Urbano)", bg="lightblue", font=("Arial", 14, "bold")).pack(pady=10)
        frame_canvas = Frame(self, bg="lightblue")
        frame_canvas.pack(fill=BOTH, expand=True, padx=5, pady=5)
        canvas = Canvas(frame_canvas, bg="lightblue", highlightthickness=0)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar = Scrollbar(frame_canvas, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollable_frame = Frame(canvas, bg="lightblue")
        canvas.create_window((0, 0), window=scrollable_frame, anchor="n")
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        scrollable_frame.imagens = [] 
        try:
            arquivos = sorted(os.listdir("img-urbano"))
            for nome_arquivo in arquivos:
                if nome_arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    caminho_completo = os.path.join("img-urbano", nome_arquivo)
                    img = Image.open(caminho_completo)
                    nova_largura = 410
                    nova_altura = int((nova_largura / img.width) * img.height)
                    img = img.resize((nova_largura, nova_altura), Image.LANCZOS)
                    photo = ImageTk.PhotoImage(img)
                    scrollable_frame.imagens.append(photo)
                    Label(scrollable_frame, image=scrollable_frame.imagens[-1]).pack(pady=10, padx=10)
        except Exception as e:
            Label(scrollable_frame, text=f"Erro ao carregar imagens: {e}", fg="red").pack()
        Button(self, text="Voltar ao Menu Principal", command=lambda: self.controller.show_frame("MainMenu")).pack(pady=10)

# =============================================================================
# --- TELA: CADASTRO URBANO ---
# =============================================================================
class CadastroUrbano(Frame):
    def __init__(self, parent, controller, view):
        super().__init__(parent, bg="lightblue")
        self.controller = controller
        self.view = view
        self.entradas = {}
        
        Label(self, text="Cadastro de Imóvel Urbano", bg="lightblue", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Frame com scroll para o formulário
        canvas_frame = Frame(self, bg="lightblue")
        canvas_frame.pack(fill="both", expand=True)
        
        canvas = Canvas(canvas_frame, bg="lightblue", highlightthickness=0)
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg="lightblue")

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Frame interno para o grid do formulário
        frame_form = Frame(scrollable_frame, bg="lightblue", padx=10, pady=10)
        frame_form.pack(expand=True)

        entry_width = 25
        
        # --- CONTEÚDO COMPLETO DO FORMULÁRIO ---
        
        # Dicionário de campos de texto
        campos_info = {
            "endereco": "Endereço:", "area_construida": "Área Construida:",
            "idade_imovel": "Idade do Imóvel:", "valor_total": "Valor Total:",
            "valor_unitario": "Valor Unitário:", "padrao_construtivo": "Padrão Construtivo:",
            "valor_residual": "Valor Residual (ex: 20):", "conservacao_foc": "*Conservação Foc:",
            "indice_fiscal": "Indice Fiscal:", "idade_referencial": "Idade Referencial em anos:",
            "estado_conservacao": "Estado de Conservação - EC:", "fator_oferta": "*Fator Oferta:",
            "padao_const": "*Padão Const.:", "conservacao": "*Conservação:",
            "localizacao": "*Localização:", "frentes_m": "*Frentes M:",
            "unitario_homog": "*Unitário Homog.:"
        }

        # Criação dos campos de texto
        row_num = 1
        for chave, texto_label in campos_info.items():
            Label(frame_form, text=texto_label, bg="lightblue").grid(row=row_num, column=0, sticky='w', pady=2, padx=5)
            self.entradas[chave] = Entry(frame_form, width=entry_width)
            self.entradas[chave].grid(row=row_num, column=1, sticky='w', pady=2, padx=5)
            row_num += 1

        # Criação dos Radiobuttons
        frentes_multiplas = StringVar(value="Não")
        frame_frentes = Frame(frame_form, bg="lightblue")
        Label(frame_frentes, text="Frentes Múltiplas:", bg="lightblue").pack(side=LEFT)
        Radiobutton(frame_frentes, text="Sim", variable=frentes_multiplas, value="Sim", bg="lightblue").pack(side=LEFT)
        Radiobutton(frame_frentes, text="Não", variable=frentes_multiplas, value="Não", bg="lightblue").pack(side=LEFT)
        frame_frentes.grid(row=row_num, column=0, columnspan=2, sticky='w', pady=5)
        self.entradas['frentes_multiplas'] = frentes_multiplas
        
        # Frame dos botões na parte inferior da tela principal do cadastro
        frame_botoes = Frame(self, bg="lightblue")
        frame_botoes.pack(pady=10)
        
        Button(frame_botoes, text="Salvar", command=self._on_save).pack(side=LEFT, padx=5)
        Button(frame_botoes, text="Cancelar", command=self._on_cancel).pack(side=LEFT, padx=5)
        Button(frame_botoes, text="Voltar", command=self._on_back).pack(side=LEFT, padx=5)

    def _on_save(self):
        dados = {}
        for key, widget in self.entradas.items():
            if isinstance(widget, StringVar):
                dados[key] = widget.get()
            else:
                dados[key] = widget.get()
        self.controller.urbano.salvar_dados(dados)
        self.limpar_formulario()
        self.controller.show_frame("MainMenu")

    def _on_cancel(self):
        self.limpar_formulario()

    def _on_back(self):
        self.controller.show_frame("MainMenu")

    def limpar_formulario(self):
        for key, widget in self.entradas.items():
            if isinstance(widget, StringVar):
                widget.set("Não")
            else:
                widget.delete(0, END)