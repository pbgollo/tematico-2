import tkinter as tk
from tkinter import messagebox

class LoginView:

    def __init__(self, root):
        self.root = root
        self.root.title("Login de Usuário")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        # Título
        self.label_login = tk.Label(root, text="Seja Bem-vindo!")
        self.label_login.place(x=157, y=30)  # Posição absoluta

        # Label e campo de e-mail
        self.label_email = tk.Label(root, text="E-mail")
        self.label_email.place(x=100, y=80)  # Label acima do campo de e-mail

        self.entry_email = tk.Entry(root)
        self.entry_email.place(x=100, y=100, width=200)  # Campo logo abaixo da label

        # Label e campo de senha
        self.label_senha = tk.Label(root, text="Senha")
        self.label_senha.place(x=100, y=140)  # Label acima do campo de senha

        self.entry_senha = tk.Entry(root, show="*")
        self.entry_senha.place(x=100, y=160, width=200)  # Campo logo abaixo da label

        # Botão de login
        self.btn_login = tk.Button(root, text="Login", command=self.login_usuario)
        self.btn_login.place(x=170, y=200)

        # Label "Não tem uma conta?"
        self.label_nao_tem_conta = tk.Label(root, text="Não tem uma conta?")
        self.label_nao_tem_conta.place(x=98, y=264)

        # Botão "Cadastre-se"
        self.btn_cadastrar = tk.Button(root, text="Cadastre-se", command=self.abrir_cadastro_view)
        self.btn_cadastrar.place(x=225, y=260)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def login_usuario(self):
        email = self.entry_email.get()
        senha = self.entry_senha.get()

        # Exibir uma mensagem temporária para o fluxo
        messagebox.showinfo("Login", f"E-mail: {email}\nTentativa de login!")

    def abrir_cadastro_view(self):
        self.root.withdraw()
        cadastro_root = tk.Toplevel(self.root)
        from views.CadastroGui import CadastroView
        CadastroView(cadastro_root)

    def on_close(self):
        self.root.destroy()