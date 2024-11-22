import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from helpers.PersonalizarWidgets import PersonalizarWidgets
from helpers.CentralizarJanela import CentralizarJanela

class EventoView:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Evento")
        self.root.configure(bg="#78d2ff")

        largura = 630
        altura = 650
        CentralizarJanela.centralizar(self.root, largura, altura)

        # Instanciar a classe de personalização
        self.personalizar = PersonalizarWidgets()

        # Criar uma lista para armazenar as referências das imagens
        self.imagens = []

        # Criar um Frame para o Canvas e Scrollbar
        frame_container = tk.Frame(self.root, bg=self.personalizar.cor_primaria)
        frame_container.pack(fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(frame_container, bg=self.personalizar.cor_primaria, bd=0, highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame_container, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, bg=self.personalizar.cor_primaria)
        self.inner_frame = tk.Frame(self.scrollable_frame, bg=self.personalizar.cor_primaria)
        self.inner_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=50, pady=20)

        self.scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="n")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.criar_widgets()


    def criar_widgets(self):
        input_width = 50
        button_width = 15

        # Título principal no topo do inner_frame
        label_titulo = tk.Label(self.inner_frame, text="Cadastro de Eventos")
        label_titulo.pack(pady=(0, 20))  # Adiciona espaçamento inferior
        self.personalizar.configurar_big_label(label_titulo)

        # Campo Nome do Evento
        label_nome_evento = tk.Label(self.inner_frame, text="Nome do Evento")
        label_nome_evento.pack(pady=(10, 0))
        self.personalizar.configurar_small_label(label_nome_evento)

        entry_nome_evento = tk.Entry(self.inner_frame, width=input_width)
        entry_nome_evento.pack(pady=(0, 10))
        self.personalizar.configurar_entry(entry_nome_evento)

        # Campo Data
        label_data = tk.Label(self.inner_frame, text="Data")
        label_data.pack(pady=(10, 0))
        self.personalizar.configurar_small_label(label_data)

        date_entry = DateEntry(
            self.inner_frame, width=48, background='#FFFFFF', 
            foreground=self.personalizar.cor_primaria, borderwidth=0, font=self.personalizar.small_font
        )
        date_entry.pack(pady=(0, 10))

        # Campo Hora
        label_hora = tk.Label(self.inner_frame, text="Hora")
        label_hora.pack(pady=(10, 0))
        self.personalizar.configurar_small_label(label_hora)

        entry_hora = tk.Entry(self.inner_frame, width=input_width)
        entry_hora.pack(pady=(0, 10))
        self.personalizar.configurar_entry(entry_hora)

        # Campo Convidados
        label_convidado = tk.Label(self.inner_frame, text="Convidados")
        label_convidado.pack(pady=(10, 0))
        self.personalizar.configurar_small_label(label_convidado)

        # Frame para o Listbox e a barra de rolagem
        frame_listbox = tk.Frame(self.inner_frame, bg=self.personalizar.cor_terciaria)
        frame_listbox.pack(pady=(0, 10))

        # Listbox para múltiplos convidados com uma barra de rolagem
        listbox_convidados = tk.Listbox(frame_listbox, selectmode=tk.MULTIPLE, height=6, width=50, bd=2, font=self.personalizar.small_font, bg="#f0f0f0", selectbackground="#ffc400", selectforeground="black", relief="flat")
        for convidado in ["João", "Maria", "Pedro", "Ana", "Carlos", "Ricardo", "Lúcia", "Fernanda", "Paulo"]:
            listbox_convidados.insert(tk.END, convidado)

        # Barra de rolagem para o Listbox
        scrollbar_convidados = tk.Scrollbar(frame_listbox, orient="vertical", command=listbox_convidados.yview)
        scrollbar_convidados.pack(side="right", fill="y")
        listbox_convidados.config(yscrollcommand=scrollbar_convidados.set)
        listbox_convidados.pack(side="left", fill="y")

        # Campo Nome do Local
        label_nome_local = tk.Label(self.inner_frame, text="Nome do Local")
        label_nome_local.pack(pady=(10, 0))
        self.personalizar.configurar_small_label(label_nome_local)

        entry_nome_local = tk.Entry(self.inner_frame, width=input_width)
        entry_nome_local.pack(pady=(0, 10))
        self.personalizar.configurar_entry(entry_nome_local)

        # Campo Rua
        label_rua = tk.Label(self.inner_frame, text="Rua")
        label_rua.pack(pady=(10, 0))
        self.personalizar.configurar_small_label(label_rua)

        entry_rua = tk.Entry(self.inner_frame, width=input_width)
        entry_rua.pack(pady=(0, 10))
        self.personalizar.configurar_entry(entry_rua)

        # Campo Número
        label_numero = tk.Label(self.inner_frame, text="Número")
        label_numero.pack(pady=(10, 0))
        self.personalizar.configurar_small_label(label_numero)

        entry_numero = tk.Entry(self.inner_frame, width=input_width)
        entry_numero.pack(pady=(0, 10))
        self.personalizar.configurar_entry(entry_numero)

        # Label "Selecione o template do convite"
        label_template = tk.Label(self.inner_frame, text="Selecione o template do convite")
        label_template.pack(pady=(20, 0))
        self.personalizar.configurar_small_label(label_template)

        # Sessão das Imagens (pode ser ajustada conforme necessário)
        frame_images = tk.Frame(self.inner_frame, bg=self.personalizar.cor_primaria)
        frame_images.pack(pady=20, anchor="center")

        def carregar_imagem(caminho):
            img = Image.open(caminho)
            img = img.resize((150, 150), Image.LANCZOS)
            return ImageTk.PhotoImage(img)

        # Caminhos das imagens (substitua pelos caminhos corretos das suas imagens)
        caminho_imagem1 = "assets/templates-backgrounds/background-1.jpg"
        caminho_imagem2 = "assets/templates-backgrounds/background-2.jpg"
        caminho_imagem3 = "assets/templates-backgrounds/background-3.jpg"

        # Carregar as imagens e armazená-las na lista self.imagens
        self.imagens.extend([
            carregar_imagem(caminho_imagem1),
            carregar_imagem(caminho_imagem2),
            carregar_imagem(caminho_imagem3)
        ])

        # Variável para rastrear a imagem selecionada
        self.imagem_selecionada = None

        # Função para selecionar a imagem e adicionar a borda
        def selecionar_imagem(label, imagem):
            if self.imagem_selecionada:
                self.imagem_selecionada.config(bd=0)
            label.config(bd=2, relief="solid", highlightthickness=2)
            self.imagem_selecionada = label
            self.imagem_selecionada_objeto = imagem

        # Adicionar as imagens ao frame com a função de seleção
        self.adicionar_imagem(frame_images, self.imagens[0], selecionar_imagem)
        self.adicionar_imagem(frame_images, self.imagens[1], selecionar_imagem)
        self.adicionar_imagem(frame_images, self.imagens[2], selecionar_imagem)

        # Função para capturar os convidados selecionados
        def enviar_dados():
            nome_evento = entry_nome_evento.get()
            data_evento = date_entry.get()
            hora_evento = entry_hora.get()

            convidados_selecionados = [listbox_convidados.get(i) for i in listbox_convidados.curselection()]
            nome_local = entry_nome_local.get()
            rua = entry_rua.get()
            numero = entry_numero.get()

            # Verificando se um template foi selecionado
            if not self.imagem_selecionada_objeto:
                messagebox.showwarning("Aviso!", "Selecione um template de convite.")
                return

            # Buscando o índice da imagem selecionada
            template_selecionado = self.imagens.index(self.imagem_selecionada_objeto)

            if not nome_evento or not data_evento or not hora_evento or not nome_local or not rua or not numero:
                messagebox.showwarning("Aviso!", "Preencha todos os campos.")
            elif not convidados_selecionados:
                messagebox.showwarning("Aviso!", "Selecione pelo menos um convidado.")
            else:
                messagebox.showinfo(
                    "Dados Enviados",
                    f"Nome do Evento: {nome_evento}\nData: {data_evento}\nHora: {hora_evento}\nConvidados: {', '.join(convidados_selecionados)}\nLocal: {nome_local}\nRua: {rua}, Número: {numero}\nTemplate Selecionado: {template_selecionado + 1}"  # Exibindo o template selecionado (1, 2, ou 3)
                )


        # Botão Enviar
        btn_enviar = tk.Button(self.inner_frame, text="Salvar", command=enviar_dados, width=button_width)
        btn_enviar.pack(pady=20)
        self.personalizar.configurar_button_amarelo(btn_enviar)

    def adicionar_imagem(self, frame, imagem, funcao_selecao):
        frame_imagem = tk.Frame(frame, bg=self.personalizar.cor_primaria)
        frame_imagem.pack(side=tk.LEFT, padx=10, anchor='center')
        
        label_imagem = tk.Label(frame_imagem, image=imagem, bd=0)
        label_imagem.pack(pady=(0, 10))

        # Passando a imagem ao invés de label
        botao_selecionar = tk.Button(frame_imagem, text="Selecionar", command=lambda: funcao_selecao(label_imagem, imagem), width=10)
        self.personalizar.configurar_button_azul(botao_selecionar, fg="white")
        botao_selecionar.pack()