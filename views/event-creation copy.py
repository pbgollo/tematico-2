import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk  # Necessário para exibir as imagens

class FormularioEvento:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulário de Evento")
        self.root.geometry("1200x700")  # Aumentar o tamanho da janela
        self.root.configure(bg="#1a70bb")  # Fundo azul da janela

        # Configurações de layout
        self.root.bind("<Configure>", self.ajustar_margem)

        # Criar uma lista para armazenar as referências das imagens
        self.imagens = []

        # Criar um Frame para o Canvas e Scrollbar
        frame_container = tk.Frame(self.root, bg="#1a70bb")
        frame_container.pack(fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(frame_container, bg="#1a70bb", bd=0, highlightthickness=0)
        scrollbar = ttk.Scrollbar(frame_container, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, bg="#1a70bb")
        self.inner_frame = tk.Frame(self.scrollable_frame, bg="#1a70bb")
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
        label_font = ("Arial", 11, "bold")
        input_font = ("Arial", 11)
        button_font = ("Arial", 10)
        input_width = 50  # Largura aumentada
        button_width = 20  # Largura aumentada para os botões
        cor_primaria = '#1a70bb'
        cor_secundaria = '#ffb224'
        cor_terceira = '#c3c3ff'

        def configurar_widget(widget, bg_color, fg_color):
            widget.config(bg=bg_color, fg=fg_color, bd=0)  # Sem borda escura

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
                messagebox.showinfo("Dados Enviados",
                                    f"Nome do Evento: {nome_evento}\nData: {data_evento}\nHora: {hora_evento}\nConvidado: {convidado_selecionado}\nLocal: {nome_local}\nRua: {rua}, Número: {numero}")

        # Campo Nome do Evento
        label_nome_evento = tk.Label(self.inner_frame, text="Nome do Evento:", font=label_font, bg=cor_primaria, fg="white")
        label_nome_evento.pack(pady=(10, 0))
        entry_nome_evento = tk.Entry(self.inner_frame, width=input_width, font=input_font, relief="flat")
        configurar_widget(entry_nome_evento, "white", "#4A4A4A")
        entry_nome_evento.pack(pady=(0, 10))

        # Campo Data
        label_data = tk.Label(self.inner_frame, text="Data:", font=label_font, bg=cor_primaria, fg="white")
        label_data.pack(pady=(10, 0))
        date_entry = DateEntry(self.inner_frame, width=48, background='#FFFFFF', foreground='#1a70bb', borderwidth=0, font=input_font)
        date_entry.pack(pady=(0, 10))

        # Campo Hora
        label_hora = tk.Label(self.inner_frame, text="Hora:", font=label_font, bg=cor_primaria, fg="white")
        label_hora.pack(pady=(10, 0))
        entry_hora = tk.Entry(self.inner_frame, width=input_width, font=input_font, relief="flat")
        configurar_widget(entry_hora, "white", "#4A4A4A")
        entry_hora.pack(pady=(0, 10))

        # Select de Convidados (Combobox)
        label_convidado = tk.Label(self.inner_frame, text="Convidado:", font=label_font, bg=cor_primaria, fg="white")
        label_convidado.pack(pady=(10, 0))
        var_convidado = tk.StringVar(self.inner_frame)
        convidados = ["João", "Maria", "Pedro", "Ana", "Carlos"]
        select_convidado = ttk.Combobox(self.inner_frame, textvariable=var_convidado, values=convidados, font=input_font, width=48)
        select_convidado.pack(pady=(0, 10))
        select_convidado.set("Selecione")

        # Campo Nome do Local
        label_nome_local = tk.Label(self.inner_frame, text="Nome do Local:", font=label_font, bg=cor_primaria, fg="white")
        label_nome_local.pack(pady=(10, 0))
        entry_nome_local = tk.Entry(self.inner_frame, width=input_width, font=input_font, relief="flat")
        configurar_widget(entry_nome_local, "white", "#4A4A4A")
        entry_nome_local.pack(pady=(0, 10))

        # Campo Rua
        label_rua = tk.Label(self.inner_frame, text="Rua:", font=label_font, bg=cor_primaria, fg="white")
        label_rua.pack(pady=(10, 0))
        entry_rua = tk.Entry(self.inner_frame, width=input_width, font=input_font, relief="flat")
        configurar_widget(entry_rua, "white", "#4A4A4A")
        entry_rua.pack(pady=(0, 10))

        # Campo Número
        label_numero = tk.Label(self.inner_frame, text="Número:", font=label_font, bg=cor_primaria, fg="white")
        label_numero.pack(pady=(10, 0))
        entry_numero = tk.Entry(self.inner_frame, width=input_width, font=input_font, relief="flat")
        configurar_widget(entry_numero, "white", "#4A4A4A")
        entry_numero.pack(pady=(0, 10))

        # Label para selecionar o template
        label_template = tk.Label(self.inner_frame, text="Selecione o template do convite:", font=label_font, bg=cor_primaria, fg="white")
        label_template.pack(pady=(20, 0))

        # Sessão das Imagens
        frame_images = tk.Frame(self.inner_frame, bg=cor_primaria)
        frame_images.pack(pady=20, anchor="center")

        def carregar_imagem(caminho):
            img = Image.open(caminho)
            img = img.resize((300, 300), Image.LANCZOS)
            return ImageTk.PhotoImage(img)

        # Caminhos das imagens (substitua pelos caminhos corretos das suas imagens)
        caminho_imagem1 = "./templates/templates-backgrounds/background-1.jpg"
        caminho_imagem2 = "./templates/templates-backgrounds/background-1.jpg"
        caminho_imagem3 = "./templates/templates-backgrounds/background-1.jpg"

        # Carregar as imagens e armazená-las na lista self.imagens
        self.imagens.append(carregar_imagem(caminho_imagem1))
        self.imagens.append(carregar_imagem(caminho_imagem2))
        self.imagens.append(carregar_imagem(caminho_imagem3))

        # Variável para rastrear a imagem selecionada
        self.imagem_selecionada = None

        # Função para selecionar a imagem e adicionar a borda
        def selecionar_imagem(label):
            if self.imagem_selecionada:
                self.imagem_selecionada.config(bd=0)
            label.config(bd=5, relief="solid", highlightbackground="blue", highlightthickness=2)
            self.imagem_selecionada = label

        # Adicionar as imagens e botões ao frame
        self.adicionar_imagem(frame_images, self.imagens[0], selecionar_imagem)
        self.adicionar_imagem(frame_images, self.imagens[1], selecionar_imagem)
        self.adicionar_imagem(frame_images, self.imagens[2], selecionar_imagem)

        # Botão de Envio (Submit)
        botao_enviar = tk.Button(self.inner_frame, text="Enviar", command=enviar_dados, width=button_width, bg=cor_secundaria, fg="white", font=button_font)
        botao_enviar.pack(pady=(30, 10))

    def adicionar_imagem(self, frame, imagem, funcao_selecao):
        frame_imagem = tk.Frame(frame, bg="#1a70bb")
        frame_imagem.pack(side=tk.LEFT, padx=10, anchor='center')
        label_imagem = tk.Label(frame_imagem, image=imagem, bd=0)
        label_imagem.pack(pady=(0, 10))
        botao = tk.Button(frame_imagem, text="Selecionar", command=lambda: funcao_selecao(label_imagem), width=20, relief="flat")
        botao.pack()

# Executar o programa
if __name__ == "__main__":
    root = tk.Tk()
    app = FormularioEvento(root)
    root.mainloop()
