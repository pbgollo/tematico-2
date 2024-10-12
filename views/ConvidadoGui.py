import tkinter as tk
from tkinter import messagebox
from utils.PersonalizarWidgets import PersonalizarWidgets
from utils.CentralizarJanela import CentralizarJanela
from controllers.ConvidadoController import ConvidadoController
from database.db import SessionLocal

class ConvidadoView:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Convidado")
        self.root.resizable(False, False)
        self.root.configure(bg="#1a70bb")

        self.session = SessionLocal()
        self.convidado_controller = ConvidadoController(self.session)

        largura = 400
        altura = 300
        CentralizarJanela.centralizar(self.root, largura, altura)

        self.personalizar = PersonalizarWidgets()

        # Título
        self.label_convidado = tk.Label(root, text="Cadastre um Convidado!")
        self.label_convidado.place(x=75, y=30)
        self.personalizar.configurar_big_label(self.label_convidado)

        # Label e campo de nome
        self.label_nome = tk.Label(root, text="Nome do Convidado")
        self.label_nome.place(x=100, y=80)  
        self.personalizar.configurar_small_label(self.label_nome)

        self.entry_nome = tk.Entry(root)
        self.entry_nome.place(x=100, y=100, width=200) 
        self.personalizar.configurar_entry(self.entry_nome)

        # Label e campo de e-mail
        self.label_email = tk.Label(root, text="E-mail do Convidado")
        self.label_email.place(x=100, y=140) 
        self.personalizar.configurar_small_label(self.label_email)

        self.entry_email = tk.Entry(root)
        self.entry_email.place(x=100, y=160, width=200)  
        self.personalizar.configurar_entry(self.entry_email)

        # Botão de cadastro
        self.btn_cadastrar = tk.Button(root, text="Cadastrar", command=self.cadastrar_convidado)
        self.btn_cadastrar.place(x=160, y=200)
        self.personalizar.configurar_button_amarelo(self.btn_cadastrar)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def cadastrar_convidado(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()

        if nome and email:
            sucesso = self.convidado_controller.cadastrar_convidado(nome, email)
            if sucesso:
                messagebox.showinfo("Cadastro", "Convidado cadastrado com sucesso!")
            else:
                messagebox.showwarning("Erro", "Convidado já cadastrado com este e-mail!")
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos!")


    def on_close(self):
        self.session.close()
        self.root.destroy()
