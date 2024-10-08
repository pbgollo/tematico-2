import tkinter as tk
from tkinter import messagebox

class CadastroView:

    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Usuário")
        self.root.geometry("450x450")
        self.root.resizable(False, False) 

        # Labels e campos com posições absolutas
        self.label_nome = tk.Label(root, text="Nome")
        self.label_nome.place(x=50, y=50)  # Posição absoluta para o label "Nome"

        self.entry_nome = tk.Entry(root)
        self.entry_nome.place(x=150, y=50, width=200)  # Campo de texto "Nome" abaixo do label

        self.label_email = tk.Label(root, text="E-mail")
        self.label_email.place(x=50, y=100)  # Posição absoluta para o label "E-mail"

        self.entry_email = tk.Entry(root)
        self.entry_email.place(x=150, y=100, width=200)  # Campo de texto "E-mail" abaixo do label

        self.label_senha = tk.Label(root, text="Senha")
        self.label_senha.place(x=50, y=150)  # Posição absoluta para o label "Senha"

        self.entry_senha = tk.Entry(root, show="*")
        self.entry_senha.place(x=150, y=150, width=200)  # Campo de texto "Senha" abaixo do label

        # Botão de cadastro
        self.btn_cadastrar = tk.Button(root, text="Cadastrar", command=self.cadastrar_usuario)
        self.btn_cadastrar.place(x=180, y=200)  # Botão "Cadastrar"

        # Label "Já possui uma conta?"
        self.label_já_conta = tk.Label(root, text="Já possui uma conta?")
        self.label_já_conta.place(x=110, y=250)  # Posição absoluta para o label "Já possui uma conta?"

        # Botão "Entre"
        self.btn_entrar = tk.Button(root, text="Entre", command=self.abrir_login_view)
        self.btn_entrar.place(x=250, y=250)  # Botão "Entre"

        # Fechar aplicação
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def cadastrar_usuario(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        senha = self.entry_senha.get()

        # Exibir uma mensagem temporária para o fluxo
        messagebox.showinfo("Cadastro", f"Nome: {nome}\nE-mail: {email}\nTentativa de cadastro!")

        # Aqui você pode adicionar a lógica para salvar o usuário no banco de dados

    def abrir_login_view(self):
        self.root.withdraw()
        login_root = tk.Toplevel(self.root)
        from views.LoginGui import LoginView
        LoginView(login_root)

    def on_close(self):
        self.root.destroy()