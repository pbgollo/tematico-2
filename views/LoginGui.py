import tkinter as tk
from tkinter import messagebox
from helpers.PersonalizarWidgets import PersonalizarWidgets
from helpers.CentralizarJanela import CentralizarJanela
from database.db import SessionLocal  
from controllers.UsuarioController import UsuarioController  

class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Login de Usuário")
        self.root.resizable(False, False)
        self.root.configure(bg="#78d2ff")

        self.session = SessionLocal()

        self.usuario_controller = UsuarioController(self.session)

        largura = 400
        altura = 330
        CentralizarJanela.centralizar(self.root, largura, altura)

        self.personalizar = PersonalizarWidgets()

        # Título
        self.label_login = tk.Label(root, text="Seja Bem-vindo!")
        self.label_login.place(x=105, y=30)
        self.personalizar.configurar_big_label(self.label_login)

        # Label e campo de e-mail
        self.label_email = tk.Label(root, text="E-mail")
        self.label_email.place(x=100, y=80)
        self.personalizar.configurar_small_label(self.label_email)

        self.entry_email = tk.Entry(root)
        self.entry_email.place(x=100, y=100, width=200)
        self.personalizar.configurar_entry(self.entry_email)

        # Label e campo de senha
        self.label_senha = tk.Label(root, text="Senha")
        self.label_senha.place(x=100, y=140)
        self.personalizar.configurar_small_label(self.label_senha)

        self.entry_senha = tk.Entry(root, show="*")
        self.entry_senha.place(x=100, y=160, width=200)
        self.personalizar.configurar_entry(self.entry_senha)

        # Botão de login
        self.btn_login = tk.Button(root, text="Login", command=self.login_usuario)
        self.btn_login.place(x=175, y=200)
        self.personalizar.configurar_button_amarelo(self.btn_login)

        # Label "Não tem uma conta?"
        self.label_nao_tem_conta = tk.Label(root, text="Não tem uma conta?")
        self.label_nao_tem_conta.place(x=75, y=264)
        self.personalizar.configurar_small_label(self.label_nao_tem_conta, fg="white", bg="#78d2ff")

        # Botão "Cadastre-se"
        self.btn_cadastrar = tk.Button(root, text="Cadastre-se", command=self.abrir_cadastro_view)
        self.btn_cadastrar.place(x=230, y=260)
        self.personalizar.configurar_button_azul(self.btn_cadastrar)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def login_usuario(self):
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        usuario = self.usuario_controller.autenticar_usuario(email, senha)
        if usuario:
            self.abrir_principal_view(usuario)
        else:
            messagebox.showerror("Login", "Usuário ou senha incorretos!")

    def abrir_principal_view(self, usuario):
        self.root.withdraw()
        principal_root = tk.Toplevel(self.root)
        from views.PrincipalGui import PrincipalView
        PrincipalView(principal_root, usuario)

    def abrir_cadastro_view(self):
        self.root.withdraw()
        cadastro_root = tk.Toplevel(self.root)
        from views.CadastroGui import CadastroView
        CadastroView(cadastro_root)

    def on_close(self):
        self.session.close()
        self.root.destroy()