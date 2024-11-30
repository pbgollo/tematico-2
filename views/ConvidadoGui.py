import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import messagebox
from controllers.ConvidadoController import ConvidadoController
from helpers.PersonalizarWidgets import PersonalizarWidgets
from helpers.CentralizarJanela import CentralizarJanela
from database.db import SessionLocal

class ConvidadoView:
    def __init__(self, root, usuario, reabrir_principal):
        self.root = root
        self.usuario = usuario
        self.reabrir_principal = reabrir_principal
        self.root.title("Gerenciar Convidados")
        self.root.resizable(False, False)
        self.root.configure(bg="#70cfff")

        self.session = SessionLocal()
        self.controller = ConvidadoController(self.session)

        largura = 500
        altura = 600
        CentralizarJanela.centralizar(self.root, largura, altura)

        self.personalizar = PersonalizarWidgets()

        # Label "Convidados"
        self.label_titulo = tk.Label(root, text="Convidados", font=("Arial", 20))
        self.label_titulo.place(x=160, y=20)
        self.personalizar.configurar_giant_label(self.label_titulo, fg="white", bg="#70cfff")

        # Label e campo de nome
        self.label_nome = tk.Label(root, text="Nome do Convidado")
        self.label_nome.place(x=150, y=80)
        self.personalizar.configurar_small_label(self.label_nome)

        self.entry_nome = tk.Entry(root)
        self.entry_nome.place(x=150, y=100, width=200)
        self.personalizar.configurar_entry(self.entry_nome)

        # Label e campo de e-mail
        self.label_email = tk.Label(root, text="E-mail do Convidado")
        self.label_email.place(x=150, y=140)
        self.personalizar.configurar_small_label(self.label_email)

        self.entry_email = tk.Entry(root)
        self.entry_email.place(x=150, y=160, width=200)
        self.personalizar.configurar_entry(self.entry_email)

        # Botão de cadastro
        self.btn_cadastrar = tk.Button(root, text="Cadastrar", command=self.cadastrar_convidado)
        self.btn_cadastrar.place(x=210, y=200)
        self.personalizar.configurar_button_amarelo(self.btn_cadastrar)

        # Frame com scroll para os convidados
        self.frame_convidados = tk.Frame(root, bg="#fafafa")
        self.frame_convidados.place(x=20, y=250, width=460, height=300)

        # Canvas para os convidados e barra de rolagem
        self.canvas_convidados = tk.Canvas(self.frame_convidados, bg="#fafafa")
        self.scrollbar = tk.Scrollbar(self.frame_convidados, orient="vertical", command=self.canvas_convidados.yview)
        self.scrollable_frame = tk.Frame(self.canvas_convidados, bg="#fafafa")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas_convidados.configure(
                scrollregion=self.canvas_convidados.bbox("all")
            )
        )

        self.canvas_convidados.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas_convidados.configure(yscrollcommand=self.scrollbar.set)

        self.canvas_convidados.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Inicializar a listagem de convidados
        self.listar_convidados()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def cadastrar_convidado(self):
        nome = self.entry_nome.get().strip()
        email = self.entry_email.get().strip()

        if not nome or not email:
            messagebox.showwarning("Campos vazios", "Preencha todos os campos.")
            return

        sucesso = self.controller.cadastrar_convidado(nome, email, self.usuario.id)
        if sucesso:
            messagebox.showinfo("Sucesso", "Convidado cadastrado com sucesso.")
            self.entry_nome.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
            self.listar_convidados()
        else:
            messagebox.showerror("Erro", "Este e-mail já está cadastrado.")

    def listar_convidados(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        convidados = self.controller.listar_convidados(self.usuario.id)
        if not convidados:
            messagebox.showinfo("Sem Convidados", "Nenhum convidado encontrado.")
            return

        largura_fixa_coluna_info = 200
        for index, convidado in enumerate(convidados):
            frame_convidado = tk.Frame(self.scrollable_frame, bg="white", relief="solid", bd=1)
            frame_convidado.grid(row=index, column=0, pady=5, padx=0, sticky="ew")
            frame_convidado.columnconfigure(1, weight=1)

            frame_info = tk.Frame(frame_convidado, bg="white", width=largura_fixa_coluna_info)
            frame_info.grid(row=0, column=1, sticky="w")
            frame_info.columnconfigure(0, weight=1)

            label_nome_convidado = tk.Label(frame_info, text=convidado.nome, bg="white", anchor="w", width=36)
            label_nome_convidado.grid(row=0, column=0, padx=5, sticky="w")
            self.personalizar.configurar_small_label(label_nome_convidado, fg="black", bg="white")

            label_email_convidado = tk.Label(frame_info, text=convidado.email, bg="white", anchor="w", width=36)
            label_email_convidado.grid(row=1, column=0, padx=5, sticky="w")
            self.personalizar.configurar_small_label(label_email_convidado, fg="grey", bg="white")

            frame_botoes = tk.Frame(frame_convidado, bg="white")
            frame_botoes.grid(row=0, column=2, sticky="e", padx=5)

            btn_remover = tk.Button(frame_botoes, text="Remover", command=lambda c=convidado.id: self.remover_convidado(c))
            btn_remover.grid(row=1, column=0, padx=5, pady=2, sticky="e")
            self.personalizar.configurar_button_amarelo(btn_remover)

    def remover_convidado(self, convidado_id):
        self.controller.excluir_convidado(convidado_id)
        messagebox.showinfo("Sucesso", "Convidado removido com sucesso.")
        self.listar_convidados()

    def on_close(self):
        self.session.close()
        self.root.destroy()
        if self.reabrir_principal:
            self.reabrir_principal()
