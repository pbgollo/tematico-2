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
        self.root.geometry("1200x700")
        self.root.configure(bg="#78d2ff")

        largura = 1200
        altura = 700
        CentralizarJanela.centralizar(self.root, largura, altura)

        # Instanciar a classe de personalização
        self.personalizar = PersonalizarWidgets()

        # Configurações de layout
        self.root.bind("<Configure>", self.ajustar_margem)

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

    def ajustar_margem(self, event):
        largura_janela = self.root.winfo_width()
        margem = max((largura_janela - 1010) // 2, 20)
        self.inner_frame.pack_configure(padx=margem)

    def criar_widgets(self):
        input_width = 50
        button_width = 20

        # Função para capturar os dados do formulário
        def enviar_dados():
            nome_evento = entry_nome_evento.get()
            data_evento = date_entry.get()
            hora_evento = entry_hora.get()
            convidado_selecionado = var_convidado.get()
            nome_local = entry_nome_local.get()
            rua = entry_rua.get()
            numero = entry_numero.get()

            if not nome_evento or not data_evento or not hora_evento or not nome_local or not rua or not numero:
                messagebox.showwarning("Aviso!", "Preencha todos os campos.")
            else:
                messagebox.showinfo(
                    "Dados Enviados",
                    f"Nome do Evento: {nome_evento}\nData: {data_evento}\nHora: {hora_evento}\nConvidado: {convidado_selecionado}\nLocal: {nome_local}\nRua: {rua}, Número: {numero}"
                )

        # Campo Nome do Evento
        label_nome_evento = tk.Label(self.inner_frame, text="Nome do Evento:")
        label_nome_evento.pack(pady=(10, 0))
        self.personalizar.configurar_small_label(label_nome_evento)

        entry_nome_evento = tk.Entry(self.inner_frame, width=input_width)
        entry_nome_evento.pack(pady=(0, 10))
        self.personalizar.configurar_entry(entry_nome_evento)

        # Campo Data
        label_data = tk.Label(self.inner_frame, text="Data:")
        label_data.pack(pady=(10, 0))
        self.personalizar.configurar_small_label(label_data)

        date_entry = DateEntry(
            self.inner_frame, width=48, background='#FFFFFF', 
            foreground=self.personalizar.cor_primaria, borderwidth=0, font=self.personalizar.small_font
        )
        date_entry.pack(pady=(0, 10))

        # Campo Hora
        label_hora = tk.Label(self.inner_frame, text="Hora:")
        label_hora.pack(pady=(10, 0))
        self.personalizar.configurar_small_label(label_hora)

        entry_hora = tk.Entry(self.inner_frame, width=input_width)
        entry_hora.pack(pady=(0, 10))
        self.personalizar.configurar_entry(entry_hora)

        # Select de Convidados (Combobox)
        label_convidado = tk.Label(self.inner_frame, text="Convidado:")
        label_convidado.pack(pady=(10, 0))
        self.personalizar.configurar_small_label(label_convidado)

        var_convidado = tk.StringVar(self.inner_frame)
        convidados = ["João", "Maria", "Pedro", "Ana", "Carlos"]
        select_convidado = ttk.Combobox(self.inner_frame, textvariable=var_convidado, values=convidados, font=self.personalizar.small_font, width=48)
        select_convidado.pack(pady=(0, 10))
        select_convidado.set("Selecione")

        # Campo Nome do Local
        label_nome_local = tk.Label(self.inner_frame, text="Nome do Local:")
        label_nome_local.pack(pady=(10, 0))
        self.personalizar.configurar_small_label(label_nome_local)

        entry_nome_local = tk.Entry(self.inner_frame, width=input_width)
        entry_nome_local.pack(pady=(0, 10))
        self.personalizar.configurar_entry(entry_nome_local)

        # Campo Rua
        label_rua = tk.Label(self.inner_frame, text="Rua:")
        label_rua.pack(pady=(10, 0))
        self.personalizar.configurar_small_label(label_rua)

        entry_rua = tk.Entry(self.inner_frame, width=input_width)
        entry_rua.pack(pady=(0, 10))
        self.personalizar.configurar_entry(entry_rua)

        # Campo Número
        label_numero = tk.Label(self.inner_frame, text="Número:")
        label_numero.pack(pady=(10, 0))
        self.personalizar.configurar_small_label(label_numero)

        entry_numero = tk.Entry(self.inner_frame, width=input_width)
        entry_numero.pack(pady=(0, 10))
        self.personalizar.configurar_entry(entry_numero)

        # Label "Selecione o template do convite"
        label_template = tk.Label(self.inner_frame, text="Selecione o template do convite:")
        label_template.pack(pady=(20, 0))
        self.personalizar.configurar_small_label(label_template)

        # Sessão das Imagens (pode ser ajustada conforme necessário)
        frame_images = tk.Frame(self.inner_frame, bg=self.personalizar.cor_primaria)
        frame_images.pack(pady=20, anchor="center")

        def carregar_imagem(caminho):
            img = Image.open(caminho)
            img = img.resize((300, 300), Image.LANCZOS)
            return ImageTk.PhotoImage(img)

        # Caminhos das imagens (substitua pelos caminhos corretos das suas imagens)
        caminho_imagem1 = "assets/templates-backgrounds/background-1.jpg"
        caminho_imagem2 = "assets/templates-backgrounds/background-2.jpg"
        caminho_imagem3 = "assets/templates-backgrounds/background-2.jpg"

        # Carregar as imagens e armazená-las na lista self.imagens
        self.imagens.extend([
            carregar_imagem(caminho_imagem1),
            carregar_imagem(caminho_imagem2),
            carregar_imagem(caminho_imagem3)
        ])

        # Variável para rastrear a imagem selecionada
        self.imagem_selecionada = None

        # Função para selecionar a imagem e adicionar a borda
        def selecionar_imagem(label):
            if self.imagem_selecionada:
                self.imagem_selecionada.config(bd=0)
            label.config(bd=5, relief="solid", highlightbackground="green", highlightthickness=2)
            self.imagem_selecionada = label

        # Adicionar as imagens ao frame com a função de seleção
        self.adicionar_imagem(frame_images, self.imagens[0], selecionar_imagem)
        self.adicionar_imagem(frame_images, self.imagens[1], selecionar_imagem)
        self.adicionar_imagem(frame_images, self.imagens[2], selecionar_imagem)

        # Botão Enviar
        btn_enviar = tk.Button(self.inner_frame, text="Enviar", command=enviar_dados, width=button_width)
        btn_enviar.pack(pady=20)
        self.personalizar.configurar_button_amarelo(btn_enviar)

    def adicionar_imagem(self, frame, imagem, funcao_selecao):
            frame_imagem = tk.Frame(frame, bg=self.personalizar.cor_primaria)
            frame_imagem.pack(side=tk.LEFT, padx=10, anchor='center')
            
            label_imagem = tk.Label(frame_imagem, image=imagem, bd=0)
            label_imagem.pack(pady=(0, 10))
        
            botao_selecionar = tk.Button(frame_imagem, text="Selecionar", command=lambda: funcao_selecao(label_imagem), width=20)
            self.personalizar.configurar_button_azul(botao_selecionar, fg="white")
            botao_selecionar.pack()

