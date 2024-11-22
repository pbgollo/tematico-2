import tkinter as tk
from tkinter import messagebox
from helpers.PersonalizarWidgets import PersonalizarWidgets
from helpers.CentralizarJanela import CentralizarJanela
from database.db import SessionLocal  

class PrincipalView:
    def __init__(self, root, usuario):
        self.root = root
        self.usuario = usuario
        self.root.title("PlanGO")
        self.root.resizable(False, False)
        self.root.configure(bg="#78d2ff")

        self.session = SessionLocal()
        
        largura = 500
        altura = 600
        CentralizarJanela.centralizar(self.root, largura, altura)

        self.personalizar = PersonalizarWidgets()

        # Label "Meus Eventos"
        self.label_titulo = tk.Label(root, text="Meus Eventos")
        self.label_titulo.place(x=150, y=20)
        self.personalizar.configurar_giant_label(self.label_titulo, fg="white", bg="#78d2ff")

        # Botão "Cadastrar novo evento"
        self.btn_cadastrar_evento = tk.Button(root, text="Cadastrar novo evento", command=self.cadastrar_evento)
        self.btn_cadastrar_evento.place(x=165, y=80, width=175)
        self.personalizar.configurar_button_azul(self.btn_cadastrar_evento)

        # Botão "Gerenciar Convidados"
        self.btn_gerenciar_convidados = tk.Button(root, text="Gerenciar Convidados", command=self.gerenciar_convidados)
        self.btn_gerenciar_convidados.place(x=165, y=120, width=175)
        self.personalizar.configurar_button_azul(self.btn_gerenciar_convidados)

        # Frame com scroll para os eventos
        self.frame_eventos = tk.Frame(root, bg="#fafafa")
        self.frame_eventos.place(x=20, y=180, width=460, height=380)

        # Canvas para os eventos e barra de rolagem
        self.canvas_eventos = tk.Canvas(self.frame_eventos, bg="#fafafa")
        self.scrollbar = tk.Scrollbar(self.frame_eventos, orient="vertical", command=self.canvas_eventos.yview)
        self.scrollable_frame = tk.Frame(self.canvas_eventos, bg="#fafafa")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas_eventos.configure(
                scrollregion=self.canvas_eventos.bbox("all")
            )
        )

        self.canvas_eventos.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas_eventos.configure(yscrollcommand=self.scrollbar.set)

        self.canvas_eventos.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Placeholder para os eventos cadastrados
        self.listar_eventos()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def listar_eventos(self):
        eventos = [
            {"nome": "Aniversário Bessegato", "data": "29/04/2025", "convidados": 8},
            {"nome": "Aniversário Gollo", "data": "29/04/2025", "convidados": 8},
            {"nome": "Aniversário Franco", "data": "29/04/2025", "convidados": 8},
            {"nome": "Aniversário Bessegato", "data": "29/04/2025", "convidados": 8},
            {"nome": "Aniversário Gollo", "data": "29/04/2025", "convidados": 8},
            {"nome": "Aniversário Franco", "data": "29/04/2025", "convidados": 8},
        ]

        if not eventos:
            messagebox.showinfo("Sem Eventos", "Nenhum evento encontrado!")
            return

        # Definir a largura fixa da coluna de informações (em pixels)
        largura_fixa_coluna_info = 250

        for index, evento in enumerate(eventos):
            # Crie o frame do evento e faça ele expandir horizontalmente
            frame_evento = tk.Frame(self.scrollable_frame, bg="white", relief="solid", bd=1)
            frame_evento.grid(row=index, column=0, pady=5, padx=0, sticky="ew")

            # Configurar a coluna do frame_evento para expandir
            frame_evento.columnconfigure(1, weight=1)

            # Imagem do evento (à esquerda)
            label_imagem = tk.Label(frame_evento, text="📅", font=("Arial", 24), bg="white", fg="red")
            label_imagem.grid(row=0, column=0, padx=5, pady=5, sticky="w")

            # Informações do evento (nome, data e convidados)
            frame_info = tk.Frame(frame_evento, bg="white", width=largura_fixa_coluna_info)
            frame_info.grid(row=0, column=1, sticky="w")
            frame_info.columnconfigure(0, weight=1)

            # Labels com largura fixa
            label_nome_evento = tk.Label(frame_info, text=evento["nome"], bg="white", anchor="w", width=largura_fixa_coluna_info // 10)
            label_nome_evento.grid(row=0, column=0, padx=5, sticky="w")
            self.personalizar.configurar_small_label(label_nome_evento, fg="black", bg="white")

            label_data_evento = tk.Label(frame_info, text=evento["data"], bg="white", anchor="w", width=largura_fixa_coluna_info // 10)
            label_data_evento.grid(row=1, column=0, padx=5, sticky="w")
            self.personalizar.configurar_small_label(label_data_evento, fg="black", bg="white")

            label_convidados = tk.Label(frame_info, text=f"{evento['convidados']} convidados", bg="white", fg="black", anchor="w", width=largura_fixa_coluna_info // 10)
            label_convidados.grid(row=2, column=0, padx=5, sticky="w")
            self.personalizar.configurar_small_label(label_convidados, fg="#878484", bg="white")

            # Frame para os botões (à direita)
            frame_botoes = tk.Frame(frame_evento, bg="white")
            frame_botoes.grid(row=0, column=2, sticky="e", padx=5)

            # Botão de editar
            btn_editar = tk.Button(frame_botoes, text="Editar", command=lambda e=evento: self.editar_evento(e))
            btn_editar.grid(row=0, column=0, padx=5, pady=2, sticky="e")
            self.personalizar.configurar_button_azul(btn_editar)

            # Botão de enviar convites
            btn_enviar_convites = tk.Button(frame_botoes, text="Enviar convites", command=lambda e=evento: self.enviar_convites(e))
            btn_enviar_convites.grid(row=1, column=0, padx=5, pady=2, sticky="e")
            self.personalizar.configurar_button_amarelo(btn_enviar_convites)

    def cadastrar_evento(self):
        # Função para abrir a view de cadastro de novo evento
        pass

    def gerenciar_convidados(self):
        # Função para abrir a view de gerenciamento de convidados
        print("Gerenciar Convidados")

    def editar_evento(self, evento):
        # Função para editar o evento
        print(f"Editando evento: {evento['nome']}")

    def enviar_convites(self, evento):
        # Função para enviar convites para o evento
        print(f"Enviando convites para: {evento['nome']}")

    def on_close(self):
        self.session.close()
        self.root.destroy()
