import tkinter as tk
from tkinter import messagebox

class FormularioConvidado:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Convidado")
        self.root.geometry("1200x600")  # Tamanho da janela ajustado
        self.root.configure(bg="#1a70bb")  # Fundo azul da janela

        # Frame principal para centralizar o conteúdo
        self.main_frame = tk.Frame(self.root, bg="#1a70bb")
        self.main_frame.pack(expand=True)  # Centralizar vertical e horizontalmente

        self.criar_widgets()

    def criar_widgets(self):
        label_font = ("Arial", 11, "bold")
        input_font = ("Arial", 11)
        button_font = ("Arial", 10)
        input_width = 40  # Ajustar largura dos campos de entrada
        button_width = 20
        cor_primaria = '#1a70bb'
        cor_secundaria = '#ffb224'

        def configurar_widget(widget, bg_color, fg_color):
            widget.config(bg=bg_color, fg=fg_color, bd=0)  # Sem borda escura

        # Função para capturar os dados do formulário
        def enviar_dados():
            nome_convidado = entry_nome_convidado.get()
            email = entry_email.get()
            if not nome_convidado or not email:
                messagebox.showwarning("Aviso!", "Preencha todos os campos.")
            else:
                messagebox.showinfo("Dados Enviados",
                                    f"Nome do convidado: {nome_convidado}\nEmail: {email}\n")

        # Campo Nome do Convidado
        label_nome_convidado = tk.Label(self.main_frame, text="Nome do Convidado:", font=label_font, bg=cor_primaria, fg="white")
        label_nome_convidado.pack(pady=(10, 0), anchor='center')  # Centralizado
        entry_nome_convidado = tk.Entry(self.main_frame, width=input_width, font=input_font, relief="flat")
        configurar_widget(entry_nome_convidado, "white", "#4A4A4A")
        entry_nome_convidado.pack(pady=(0, 10), anchor='center')

        # Campo Email
        label_email = tk.Label(self.main_frame, text="E-mail:", font=label_font, bg=cor_primaria, fg="white")
        label_email.pack(pady=(10, 0), anchor='center')  # Centralizado
        entry_email = tk.Entry(self.main_frame, width=input_width, font=input_font, relief="flat")
        configurar_widget(entry_email, "white", "#4A4A4A")
        entry_email.pack(pady=(0, 10), anchor='center')

        # Botão de Envio (Submit)
        botao_enviar = tk.Button(self.main_frame, text="Cadastrar", command=enviar_dados, width=button_width, bg=cor_secundaria, fg="white", font=button_font)
        botao_enviar.pack(pady=(30, 10), anchor='center')  # Centralizado

# Executar o programa
if __name__ == "__main__":
    root = tk.Tk()
    app = FormularioConvidado(root)
    root.mainloop()
