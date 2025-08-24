
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
        for F in (MainMenu, TabelaUrbana, CadastroUrbano, AtualizacaoUrbana, CadastroRural, TabelaRural):
            page_name = F.__name__
            frame = F(container, controller=self.controller, view=self)
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
    
    def show_error(self, title, message):
        messagebox.showerror(title, message)

# =============================================================================
# --- TELA: MENU PRINCIPAL ---
# =============================================================================
class MainMenu(Frame):
    def __init__(self, parent, controller, view):
        super().__init__(parent, bg="lightblue")
        self.controller = controller
        self.view = view

        # --- Frame para os Radio Buttons ---
        frame_opcoes = Frame(self, bg="lightblue")
        frame_opcoes.pack(pady=10, padx=20, fill='x', expand=True)
        Label(frame_opcoes, text="Informe o tipo de avaliação:", bg="lightblue").pack(anchor='center')
        frame_radios = Frame(frame_opcoes, bg="lightblue")
        frame_radios.pack(anchor='center')
        
        # O comando do radio button agora chama uma função do controller para trocar a tabela
        Radiobutton(frame_radios, text="Urbano", variable=self.view.tipo_avaliacao, value="urbano", bg="lightblue", command=self.controller.switch_tree_view).pack(side=LEFT)
        Radiobutton(frame_radios, text="Imóveis Rurais", variable=self.view.tipo_avaliacao, value="rural", bg="lightblue", command=self.controller.switch_tree_view).pack(side=LEFT)
        
        # --- Frame para os Botões Principais ---
        frame_botoes = Frame(self, bg="lightblue")
        frame_botoes.pack(pady=5, padx=20, fill='x', expand=True)
        estilo_botao = {"bg": "#007BFF", "fg": "white", "font": ("Arial", 10, "bold"), "relief": "raised", "borderwidth": 2, "width": 15}
        Button(frame_botoes, text="Novo Calculo", command=self.controller.iniciar_novo_calculo, **estilo_botao).pack(pady=4)
        Button(frame_botoes, text="Tabelas", command=self.controller.mostrar_tabelas, **estilo_botao).pack(pady=4)
        Button(frame_botoes, text="Atualizar", command=self.controller.iniciar_atualizacao, **estilo_botao).pack(pady=4)
        Button(frame_botoes, text="Delete", command=self.controller.deletar_dados, **estilo_botao).pack(pady=4)
        Button(frame_botoes, text="Sair", command=self.controller.sair, **estilo_botao).pack(pady=4)
        
        # --- Container para as Treeviews ---
        self.frame_treeview_container = Frame(self, bg="lightblue")
        self.frame_treeview_container.pack(pady=10, padx=10, fill='both', expand=True)
        self.frame_treeview_container.grid_rowconfigure(0, weight=1)
        self.frame_treeview_container.grid_columnconfigure(0, weight=1)

        self._criar_treeview_urbana()
        self._criar_treeview_rural()

<<<<<<< HEAD
        # --- Frame para o Valor Unitário Médio ---
=======
        for cid, cheading in self.colunas_info:
            self.tree.heading(cid, text=cheading)
            self.tree.column(cid, width=120, anchor='center') # Largura padrão para cada coluna
        
        # Scrollbar Vertical
        scrollbar_y = ttk.Scrollbar(frame_treeview, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar_y.set)
        
        # Scrollbar Horizontal
        scrollbar_x = ttk.Scrollbar(frame_treeview, orient=HORIZONTAL, command=self.tree.xview)
        self.tree.configure(xscrollcommand=scrollbar_x.set)

        # Empacotando os widgets na ordem correta
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        self.tree.pack(fill='both', expand=True)
        

        # --- CÓDIGO DO VALOR UNITÁRIO MÉDIO ESTÁ AQUI ---
        # --- FRAME PARA O RESULTADO DO VALOR UNITÁRIO MÉDIO ---
>>>>>>> 418caafe8c516dfa7548ff673b672bb638a7f75c
        frame_resultado = Frame(self, bg="lightblue")
        frame_resultado.pack(pady=5, padx=10, fill='x')
        Label(frame_resultado, text="Valor Unitario Médio:", bg="lightblue", font=("Arial", 10, "bold")).pack(side=LEFT, padx=5)
        self.valor_unitario_medio_var = StringVar()
        Entry(frame_resultado, textvariable=self.valor_unitario_medio_var, width=30, state='readonly', font=("Arial", 10, "bold"), readonlybackground='white', fg='black').pack(side=LEFT, padx=5)

        # Mostra a treeview urbana por padrão
        self.show_tree('urbano')

    def _criar_treeview_urbana(self):
        self.frame_urbano = Frame(self.frame_treeview_container)
        colunas_info = [
            ("endereco", "Endereço"), ("area_construida", "Área"), ("idade_imovel", "Idade"), 
            ("valor_total", "Valor Total"), ("valor_unitario", "Valor Unitário"), ("padrao_construtivo", "Padrão"),
            ("valor_residual", "Residual"), ("conservacao_foc", "*Cons. Foc"), ("indice_fiscal", "Indice Fiscal"),
            ("frentes_multiplas", "Frentes Múlt."), ("idade_referencial", "Idade Ref."), ("estado_conservacao", "Est. Conservação"),
            ("fator_oferta", "*Fator Oferta"), ("padao_const", "*Padrão Const."), ("conservacao", "*Conservação"),
            ("localizacao", "*Localização"), ("frentes_m", "*Frentes M"), ("unitario_homog", "*Unitário Homog."),
            ("benfeitorias", "Benfeitorias")
        ]
        self.colunas_urbano = [c[0] for c in colunas_info]
        self.tree_urbano = ttk.Treeview(self.frame_urbano, columns=self.colunas_urbano, show='headings')
        for cid, cheading in colunas_info:
            self.tree_urbano.heading(cid, text=cheading, anchor='center')
            self.tree_urbano.column(cid, width=120, anchor='center')
        
        # Scrollbars
        scrollbar_y = ttk.Scrollbar(self.frame_urbano, orient=VERTICAL, command=self.tree_urbano.yview)
        scrollbar_x = ttk.Scrollbar(self.frame_urbano, orient=HORIZONTAL, command=self.tree_urbano.xview)
        self.tree_urbano.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        self.tree_urbano.pack(fill='both', expand=True)

    def _criar_treeview_rural(self):
        self.frame_rural = Frame(self.frame_treeview_container)
        colunas_info = [
            ("area_imovel", "Área do Imóvel(m2)"), ("valor_imovel_sem_benf", "Valor Imóvel sem Benf.(R$)"),
            ("valor_unitario", "Valor Unitário"), ("fonte", "Fonte"),
            ("nota_agronomica", "Nota Agronômica"), ("unitario_homog", "Unitário Homog.")
        ]
        self.colunas_rural = [c[0] for c in colunas_info]
        self.tree_rural = ttk.Treeview(self.frame_rural, columns=self.colunas_rural, show='headings')
        for cid, cheading in colunas_info:
            self.tree_rural.heading(cid, text=cheading, anchor='center')
            self.tree_rural.column(cid, width=150, anchor='center')
        
        # Scrollbars
        scrollbar_y = ttk.Scrollbar(self.frame_rural, orient=VERTICAL, command=self.tree_rural.yview)
        scrollbar_x = ttk.Scrollbar(self.frame_rural, orient=HORIZONTAL, command=self.tree_rural.xview)
        self.tree_rural.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        scrollbar_y.pack(side=RIGHT, fill=Y)
        scrollbar_x.pack(side=BOTTOM, fill=X)
        self.tree_rural.pack(fill='both', expand=True)

    def show_tree(self, mode):
        if mode == 'urbano':
            self.frame_urbano.grid(row=0, column=0, sticky="nsew")
            self.frame_rural.grid_remove()
        elif mode == 'rural':
            self.frame_rural.grid(row=0, column=0, sticky="nsew")
            self.frame_urbano.grid_remove()

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
                    nova_largura = 650 
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
        
        frame_form = Frame(scrollable_frame, bg="lightblue", padx=10, pady=10)
        frame_form.pack(expand=True)

        entry_width = 25
        
        tipo_cadastro = StringVar(value="avaliando")
        frame_tipo_cadastro = Frame(frame_form, bg="lightblue")
        Label(frame_tipo_cadastro, text="Tipo de Cadastro:", bg="lightblue").pack(side=LEFT)
        Radiobutton(frame_tipo_cadastro, text="Avaliando", variable=tipo_cadastro, value="avaliando", bg="lightblue").pack(side=LEFT)
        Radiobutton(frame_tipo_cadastro, text="Amostra", variable=tipo_cadastro, value="amostra", bg="lightblue").pack(side=LEFT)
        frame_tipo_cadastro.grid(row=0, column=0, columnspan=2, sticky='w', pady=5)
        self.entradas['tipo_cadastro'] = tipo_cadastro

        campos_info = {
            "endereco": "Endereço:", "area_construida": "Área Construida:",
            "idade_imovel": "Idade do Imóvel:", "valor_total": "Valor Total:",
            "valor_unitario": "Valor Unitário:", "padrao_construtivo": "Padrão Construtivo:",
            "valor_residual": "Valor Residual (ex: 20):", "conservacao_foc": "*Conservação Foc:",
            "indice_fiscal": "Indice Fiscal:"
        }
        
        row_num = 1
        for chave, texto_label in campos_info.items():
            Label(frame_form, text=texto_label, bg="lightblue").grid(row=row_num, column=0, sticky='w', pady=2, padx=5)
            self.entradas[chave] = Entry(frame_form, width=entry_width)
            self.entradas[chave].grid(row=row_num, column=1, sticky='w', pady=2, padx=5)
            row_num += 1

        frentes_multiplas = StringVar(value="Não")
        frame_frentes = Frame(frame_form, bg="lightblue")
        Label(frame_frentes, text="Frentes Múltiplas:", bg="lightblue").pack(side=LEFT)
        Radiobutton(frame_frentes, text="Sim", variable=frentes_multiplas, value="Sim", bg="lightblue").pack(side=LEFT)
        Radiobutton(frame_frentes, text="Não", variable=frentes_multiplas, value="Não", bg="lightblue").pack(side=LEFT)
        frame_frentes.grid(row=row_num, column=0, columnspan=2, sticky='w', pady=5)
        self.entradas['frentes_multiplas'] = frentes_multiplas
        row_num += 1

        campos_info_2 = {
            "idade_referencial": "Idade Referencial em anos:",
            "estado_conservacao": "Estado de Conservação - EC:", "fator_oferta": "*Fator Oferta:",
            "padao_const": "*Padão Const.:", "conservacao": "*Conservação:",
            "localizacao": "*Localização:", "frentes_m": "*Frentes M:",
            "unitario_homog": "*Unitário Homog.:",
            "benfeitorias": "Benfeitorias (Float):", # <-- NOVO CAMPO ADICIONADO
            "descricao_benfeitorias": "Descrição Benfeitorias:" # <-- NOVO CAMPO ADICIONADO
        }

        for chave, texto_label in campos_info_2.items():
            Label(frame_form, text=texto_label, bg="lightblue").grid(row=row_num, column=0, sticky='w', pady=2, padx=5)
            self.entradas[chave] = Entry(frame_form, width=entry_width)
            self.entradas[chave].grid(row=row_num, column=1, sticky='w', pady=2, padx=5)
            row_num += 1

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

# =============================================================================
# --- NOVA TELA: TABELA RURAL (IMAGENS) ---
# =============================================================================
class TabelaRural(Frame):
    def __init__(self, parent, controller, view):
        super().__init__(parent, bg="lightblue")
        self.controller = controller
        self.view = view
        self.imagens_carregadas = False

    def on_show(self):
        # Este método é chamado toda vez que a tela é exibida
        if not self.imagens_carregadas:
            self.carregar_conteudo()
            self.imagens_carregadas = True

    def carregar_conteudo(self):
        Label(self, text="Tabelas de Referência (Rural)", bg="lightblue", font=("Arial", 14, "bold")).pack(pady=10)
        
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
            # Procura imagens na pasta img-rural
            arquivos = sorted(os.listdir("img-rural"))
            for nome_arquivo in arquivos:
                if nome_arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    caminho_completo = os.path.join("img-rural", nome_arquivo)
                    img = Image.open(caminho_completo)
                    
                    # Ajusta a largura da imagem
                    nova_largura = 650
                    nova_altura = int((nova_largura / img.width) * img.height)
                    img = img.resize((nova_largura, nova_altura), Image.LANCZOS)

                    photo = ImageTk.PhotoImage(img)
                    scrollable_frame.imagens.append(photo)
                    
                    Label(scrollable_frame, image=scrollable_frame.imagens[-1]).pack(pady=10, padx=10)
        except Exception as e:
            Label(scrollable_frame, text=f"Erro ao carregar imagens: {e}", fg="red").pack()
        
        Button(self, text="Voltar ao Menu Principal", command=lambda: self.controller.show_frame("MainMenu")).pack(pady=10)


# =============================================================================
# --- CORREÇÃO DO NameError: CLASSE AtualizacaoUrbana ADICIONADA ---
# =============================================================================
class AtualizacaoUrbana(Frame):
    def __init__(self, parent, controller, view):
        super().__init__(parent, bg="lightblue")
        self.controller = controller
        self.view = view
        self.entradas = {}

        Label(self, text="Atualizar Cadastro de Imóvel", bg="lightblue", font=("Arial", 14, "bold")).pack(pady=10)
        
        # A estrutura do formulário é idêntica à do CadastroUrbano
        # Você pode copiar o código de criação do formulário de CadastroUrbano para cá
        # Por simplicidade, vou criar apenas alguns campos de exemplo
        frame_form = Frame(self, bg="lightblue")
        frame_form.pack(pady=10, padx=10)
        Label(frame_form, text="Endereço:", bg="lightblue").grid(row=0, column=0)
        self.entradas['endereco'] = Entry(frame_form)
        self.entradas['endereco'].grid(row=0, column=1)

        # BOTÕES DIFERENTES
        frame_botoes = Frame(self, bg="lightblue")
        frame_botoes.pack(pady=10)
        
        Button(frame_botoes, text="Atualizar", command=self._on_update).pack(side=LEFT, padx=5)
        Button(frame_botoes, text="Cancelar", command=self._on_cancel).pack(side=LEFT, padx=5)

    def popular_formulario(self, dados):
        """Preenche os campos do formulário com os dados existentes."""
        for chave, widget in self.entradas.items():
            valor = dados.get(chave, "")
            if isinstance(widget, StringVar):
                widget.set(valor)
            else:
                widget.delete(0, END)
                widget.insert(0, valor)

    def _on_update(self):
        dados_atualizados = {key: widget.get() for key, widget in self.entradas.items()}
        self.controller.urbano.executar_atualizacao(dados_atualizados)
        self.controller.show_frame("MainMenu")

    def _on_cancel(self):
        self.controller.show_frame("MainMenu")

# =============================================================================
# --- NOVA TELA: CADASTRO RURAL ---
# =============================================================================
class CadastroRural(Frame):
    def __init__(self, parent, controller, view):
        super().__init__(parent, bg="lightblue")
        self.controller = controller
        self.view = view
        self.entradas = {}
        
        Label(self, text="Cadastro de Imóvel Rural", bg="lightblue", font=("Arial", 14, "bold")).pack(pady=10)
        
        frame_form = Frame(self, bg="lightblue", padx=10, pady=10)
        frame_form.pack(expand=True)

        entry_width = 25
        
        # --- Campos do Formulário ---
        # Tipo de Cadastro
        tipo_cadastro = StringVar(value="avaliando")
        frame_tipo_cadastro = Frame(frame_form, bg="lightblue")
        Label(frame_tipo_cadastro, text="Tipo de Cadastro:", bg="lightblue").pack(side=LEFT)
        Radiobutton(frame_tipo_cadastro, text="Avaliando", variable=tipo_cadastro, value="avaliando", bg="lightblue").pack(side=LEFT)
        Radiobutton(frame_tipo_cadastro, text="Amostra", variable=tipo_cadastro, value="amostra", bg="lightblue").pack(side=LEFT)
        frame_tipo_cadastro.grid(row=0, column=0, columnspan=2, sticky='w', pady=5)
        self.entradas['tipo_cadastro'] = tipo_cadastro

        # Dicionário de campos de texto
        campos_info = {
            "area_imovel": "Área do Imóvel(m2):",
            "valor_imovel_sem_benf": "Valor do Imóvel sem Benf.(R$):",
            "benfeitorias": "Benfeitorias:",
            "valor_unitario": "Valor Unitario (R$/m2):",
            "fonte": "Fonte(1,0 ou 0,9):",
            "fator_na": "Fator(N.A):",
            "nota_agronomica": "Nota Agronômica:",
            "unitario_homog": "Unitário Homog. (R$/m2):"
        }
        
        row_num = 1
        for chave, texto_label in campos_info.items():
            Label(frame_form, text=texto_label, bg="lightblue").grid(row=row_num, column=0, sticky='w', pady=2, padx=5)
            self.entradas[chave] = Entry(frame_form, width=entry_width)
            self.entradas[chave].grid(row=row_num, column=1, sticky='w', pady=2, padx=5)
            row_num += 1

        # --- Seção Classe de Uso do Solo ---
        frame_classes = LabelFrame(frame_form, text=" Classe de Uso do Solo (Colocar o % para cada Classe) ", bg="lightblue", padx=10, pady=10)
        frame_classes.grid(row=row_num, column=0, columnspan=2, sticky='w', pady=10, padx=5)
        
        for i in range(1, 9):
            chave = f"classe_{i}"
            Label(frame_classes, text=f"Classe {i} -", bg="lightblue").grid(row=i-1, column=0, sticky='w', pady=2)
            self.entradas[chave] = Entry(frame_classes, width=10)
            self.entradas[chave].grid(row=i-1, column=1, sticky='w', pady=2)

        # --- Botões de Ação ---
        frame_botoes = Frame(self, bg="lightblue")
        frame_botoes.pack(pady=10)
        
        Button(frame_botoes, text="Salvar", command=self._on_save).pack(side=LEFT, padx=5)
        Button(frame_botoes, text="Cancelar", command=self._on_cancel).pack(side=LEFT, padx=5)
        Button(frame_botoes, text="Voltar", command=self._on_back).pack(side=LEFT, padx=5)

    def _on_save(self):
        dados = {}
        for key, widget in self.entradas.items():
            dados[key] = widget.get()
        
        # Chama o controller RURAL para salvar
        self.controller.rural.salvar_dados(dados)
        self.limpar_formulario()
        self.controller.show_frame("MainMenu")

    def _on_cancel(self):
        self.limpar_formulario()

    def _on_back(self):
        self.controller.show_frame("MainMenu")

    def limpar_formulario(self):
        for key, widget in self.entradas.items():
            if isinstance(widget, StringVar):
                widget.set("avaliando")
            else:
                widget.delete(0, END)

