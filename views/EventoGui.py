import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from controllers.EventoController import EventoController
from controllers.ConvidadoController import ConvidadoController
from helpers.PersonalizarWidgets import PersonalizarWidgets
from helpers.CentralizarJanela import CentralizarJanela
from database.db import SessionLocal
from models.EventoConvidadoModel import EventoConvidado

class EventoView:
    def __init__(self, root, usuario, principal_view_callback):
        self.root = root
        self.usuario = usuario
        self.principal_view_callback = principal_view_callback
        self.root.title("Cadastro de Evento")
        self.root.configure(bg="#70cfff")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
        self.session = SessionLocal()
        
        self.convidado_controller = ConvidadoController(self.session)
        self.evento_controller = EventoController(self.session)

        largura = 630
        altura = 650
        CentralizarJanela.centralizar(self.root, largura, altura)

        # Instanciar a classe de personalização
        self.personalizar = PersonalizarWidgets()

        # Criar uma lista para armazenar as referências das imagens
        self.imagens = []
        self.botoes_template = []

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
        listbox_convidados = tk.Listbox(frame_listbox, selectmode=tk.MULTIPLE, height=6, width=50, bd=2, font=self.personalizar.small_font, bg="#f0f0f0", selectbackground="#02ba4f", selectforeground="black", relief="flat")
        
        convidados = self.convidado_controller.listar_convidados(self.usuario.id)
        
        for convidado in convidados:
            nome_email = convidado.nome + " (" + convidado.email + ")"
            listbox_convidados.insert(tk.END, nome_email)

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

        # Campo Endereço
        label_endereco = tk.Label(self.inner_frame, text="Endereço")
        label_endereco.pack(pady=(10, 0))
        self.personalizar.configurar_small_label(label_endereco)

        entry_endereco = tk.Entry(self.inner_frame, width=input_width)
        entry_endereco.pack(pady=(0, 10))
        self.personalizar.configurar_entry(entry_endereco)

        # Campo Comidas
        label_comida = tk.Label(self.inner_frame, text="Comidas")
        label_comida.pack(pady=(10, 0))
        self.personalizar.configurar_small_label(label_comida)

        entry_comida = tk.Entry(self.inner_frame, width=input_width)
        entry_comida.pack(pady=(0, 10))
        self.personalizar.configurar_entry(entry_comida)
        
        # Campo bebidas
        label_bebida = tk.Label(self.inner_frame, text="Bebida")
        label_bebida.pack(pady=(10, 0))
        self.personalizar.configurar_small_label(label_bebida)

        entry_bebida = tk.Entry(self.inner_frame, width=input_width)
        entry_bebida.pack(pady=(0, 10))
        self.personalizar.configurar_entry(entry_bebida)

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

        # Função para selecionar o template do convite
        def selecionar_imagem(botao, imagem):
            # Resetar o estado de todos os botões
            for b in self.botoes_template:
                b.config(text="Selecionar", bg=self.personalizar.cor_terciaria, fg="white")

            # Atualizar o botão clicado
            botao.config(text="Selecionado", bg="#02ba4f", fg="white")
            self.imagem_selecionada = imagem

        # Adicionar as imagens ao frame com a função de seleção
        self.adicionar_imagem(frame_images, self.imagens[0], selecionar_imagem)
        self.adicionar_imagem(frame_images, self.imagens[1], selecionar_imagem)
        self.adicionar_imagem(frame_images, self.imagens[2], selecionar_imagem)

        def enviar_dados():
            nome_evento = entry_nome_evento.get()
            data_evento = date_entry.get()
            hora_evento = entry_hora.get()
            convidados_selecionados = [listbox_convidados.get(i) for i in listbox_convidados.curselection()]
            nome_local = entry_nome_local.get()
            endereco = entry_endereco.get()
            comida = entry_comida.get()
            bebida = entry_bebida.get()

            if not self.imagem_selecionada:
                messagebox.showwarning("Aviso!", "Selecione um template de convite.")
                return

            template_selecionado = self.imagens.index(self.imagem_selecionada)

            if not nome_evento or not data_evento or not hora_evento or not nome_local or not endereco or not comida or not bebida:
                messagebox.showwarning("Aviso!", "Preencha todos os campos.")
            elif not convidados_selecionados:
                messagebox.showwarning("Aviso!", "Selecione pelo menos um convidado.")
            else:
                try:
                    # Cadastrar evento e obter ID do evento recém-criado
                    evento_id = self.evento_controller.adicionar_evento(
                        nome=nome_evento,
                        data=data_evento,
                        hora=hora_evento,
                        local=nome_local,
                        endereco=endereco,
                        comida=comida,
                        bebida=bebida,
                        template_id=template_selecionado + 1,
                        id_usuario=self.usuario.id
                    )
                    
                    emails_convidados = [convidado.split('(')[-1].strip(')') for convidado in convidados_selecionados]
                    
                    self.evento_controller.adicionar_convidados(evento_id, emails_convidados)

                    messagebox.showinfo("Sucesso", "Evento cadastrado com sucesso!")
                    
                    self.root.destroy()
                    if self.principal_view_callback:
                        self.principal_view_callback()
                except Exception as e:
                    messagebox.showerror("Erro", f"Erro ao cadastrar evento: {str(e)}")



        # Botão Enviar
        btn_enviar = tk.Button(self.inner_frame, text="Salvar", command=enviar_dados, width=button_width)
        btn_enviar.pack(pady=20)
        self.personalizar.configurar_button_amarelo(btn_enviar)

    def adicionar_imagem(self, frame, imagem, funcao_selecao):
        frame_imagem = tk.Frame(frame, bg=self.personalizar.cor_primaria)
        frame_imagem.pack(side=tk.LEFT, padx=10, anchor='center')
        
        label_imagem = tk.Label(frame_imagem, image=imagem, bd=0)
        label_imagem.pack(pady=(0, 10))

        # Botão para selecionar o template
        botao_selecionar = tk.Button(
            frame_imagem, 
            text="Selecionar", 
            command=lambda: funcao_selecao(botao_selecionar, imagem), 
            width=10
        )
        self.personalizar.configurar_button_azul(botao_selecionar, fg="white")
        botao_selecionar.pack()

        # Adicionar o botão à lista de botões
        self.botoes_template.append(botao_selecionar)
        
    def on_close(self):
        self.session.close()
        self.root.destroy()
        if self.principal_view_callback:
            self.principal_view_callback()
