import tkinter as tk
from tkinter import messagebox
from helpers.PersonalizarWidgets import PersonalizarWidgets
from helpers.CentralizarJanela import CentralizarJanela
from controllers.UsuarioController import UsuarioController
from database.db import SessionLocal 

class CadastroView:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Usuário")
        self.root.resizable(False, False)
        self.root.configure(bg="#78d2ff")

        self.session = SessionLocal()
        self.usuario_controller = UsuarioController(self.session)

        largura = 400
        altura = 380
        CentralizarJanela.centralizar(self.root, largura, altura)

        self.personalizar = PersonalizarWidgets()

        # Título
        self.label_cadastro = tk.Label(root, text="Vamos criar a sua conta!")
        self.label_cadastro.place(x=55, y=30)
        self.personalizar.configurar_big_label(self.label_cadastro)

        # Label e campo de nome
        self.label_nome = tk.Label(root, text="Nome")
        self.label_nome.place(x=100, y=80)  
        self.personalizar.configurar_small_label(self.label_nome)

        self.entry_nome = tk.Entry(root)
        self.entry_nome.place(x=100, y=100, width=200) 
        self.personalizar.configurar_entry(self.entry_nome)

        # Label e campo de e-mail
        self.label_email = tk.Label(root, text="E-mail")
        self.label_email.place(x=100, y=140) 
        self.personalizar.configurar_small_label(self.label_email)

        self.entry_email = tk.Entry(root)
        self.entry_email.place(x=100, y=160, width=200)  
        self.personalizar.configurar_entry(self.entry_email)

        # Label e campo de senha
        self.label_senha = tk.Label(root, text="Senha")
        self.label_senha.place(x=100, y=200)  
        self.personalizar.configurar_small_label(self.label_senha)

        self.entry_senha = tk.Entry(root, show="*")
        self.entry_senha.place(x=100, y=220, width=200)  
        self.personalizar.configurar_entry(self.entry_senha)

        # Botão de cadastro
        self.btn_cadastrar = tk.Button(root, text="Cadastrar", command=self.cadastrar_usuario)
        self.btn_cadastrar.place(x=160, y=260)
        self.personalizar.configurar_button_amarelo(self.btn_cadastrar)

        # Label "Já possui uma conta?"
        self.label_ja_conta = tk.Label(root, text="Já possui uma conta?")
        self.label_ja_conta.place(x=90, y=320)
        self.personalizar.configurar_small_label(self.label_ja_conta, fg="white", bg="#78d2ff")

        # Botão "Entre"
        self.btn_entrar = tk.Button(root, text="Entre", command=self.abrir_login_view)
        self.btn_entrar.place(x=255, y=316)
        self.personalizar.configurar_button_azul(self.btn_entrar)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def cadastrar_usuario(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        senha = self.entry_senha.get()

        if nome and email and senha:
            sucesso = self.usuario_controller.cadastrar_usuario(nome, email, senha)
            if sucesso:
                messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
            else:
                messagebox.showwarning("Erro", "E-mail já cadastrado!")
        else:
            messagebox.showwarning("Erro", "Preencha todos os campos!")

    def abrir_login_view(self):
        self.root.withdraw()
        login_root = tk.Toplevel(self.root)
        from views.LoginGui import LoginView
        LoginView(login_root)

    def on_close(self):
        self.session.close()
        self.root.destroy()