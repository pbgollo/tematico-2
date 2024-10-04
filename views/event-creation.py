import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk  # Necessário para exibir as imagens

# Função para capturar os dados do formulário
def enviar_dados():
    nome_evento = entry_nome_evento.get()
    data_evento = date_entry.get()
    hora_evento = entry_hora.get()
    convidado_selecionado = var_convidado.get()
    nome_local = entry_nome_local.get()
    rua = entry_rua.get()
    numero = entry_numero.get()

    # Verificar se todos os campos estão preenchidos
    if not nome_evento or not data_evento or not hora_evento or not nome_local or not rua or not numero:
        messagebox.showwarning("Aviso!", "Preencha todos os campos.")
    else:
        # Exibir mensagem com os dados capturados
        messagebox.showinfo("Dados Enviados",
                            f"Nome do Evento: {nome_evento}\nData: {data_evento}\nHora: {hora_evento}\nConvidado: {convidado_selecionado}\nLocal: {nome_local}\nRua: {rua}, Número: {numero}")

# Função para ajustar a margem com base na largura da janela
def ajustar_margem(event):
    largura_janela = root.winfo_width()
    margem = max((largura_janela - 1010) // 2, 20)  # Ajusta a margem para centralizar, mínimo de 20px
    inner_frame.pack_configure(padx=margem)  # Atualiza a margem esquerda/direita

# Criar a janela principal
root = tk.Tk()
root.title("Formulário de Evento")
root.geometry("1200x700")  # Aumentar o tamanho da janela
root.configure(bg="#1a70bb")  # Fundo azul da janela

# Detectar redimensionamento da janela
root.bind("<Configure>", ajustar_margem)

# Criar um Frame para o Canvas e Scrollbar
frame_container = tk.Frame(root, bg="#1a70bb")
frame_container.pack(fill=tk.BOTH, expand=True)

# Criar Canvas com Scrollbar
canvas = tk.Canvas(frame_container, bg="#1a70bb", bd=0, highlightthickness=0)
scrollbar = ttk.Scrollbar(frame_container, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg="#1a70bb")
inner_frame = tk.Frame(scrollable_frame, bg="#1a70bb")
inner_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=50, pady=20)  # Expansão e preenchimento automático

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="n")
canvas.configure(yscrollcommand=scrollbar.set)

# Adicionar Canvas e Scrollbar ao Frame Container
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Aumentar a largura dos inputs e botões em cerca de 20px
input_width = 50  # Largura aumentada
button_width = 20  # Largura aumentada para os botões

label_font = ("Arial", 11, "bold")
input_font = ("Arial", 11)
button_font = ("Arial", 10)

cor_primaria = '#1a70bb'
cor_secundaria = '#ffb224'
cor_terceira = '#c3c3ff'

# Função para configurar o estilo de botões e inputs
def configurar_widget(widget, bg_color, fg_color):
    widget.config(bg=bg_color, fg=fg_color, bd=0)  # Sem borda escura

# Criar os widgets dentro do inner_frame usando pack para organizar verticalmente
# Campo Nome do Evento
label_nome_evento = tk.Label(inner_frame, text="Nome do Evento:", font=label_font, bg=cor_primaria, fg="white")
label_nome_evento.pack(pady=(10, 0))
entry_nome_evento = tk.Entry(inner_frame, width=input_width, font=input_font, relief="flat")
configurar_widget(entry_nome_evento, "white", "#4A4A4A")  # Fundo branco, texto cinza escuro
entry_nome_evento.pack(pady=(0, 10))

# Campo Data
label_data = tk.Label(inner_frame, text="Data:", font=label_font, bg=cor_primaria, fg="white")
label_data.pack(pady=(10, 0))
date_entry = DateEntry(inner_frame, width=48, background='#FFFFFF', foreground='#1a70bb', borderwidth=0, font=input_font)
date_entry.pack(pady=(0, 10))

# Campo Hora
label_hora = tk.Label(inner_frame, text="Hora:", font=label_font, bg=cor_primaria, fg="white")
label_hora.pack(pady=(10, 0))
entry_hora = tk.Entry(inner_frame, width=input_width, font=input_font, relief="flat")
configurar_widget(entry_hora, "white", "#4A4A4A")
entry_hora.pack(pady=(0, 10))

# Select de Convidados (Combobox)
label_convidado = tk.Label(inner_frame, text="Convidado:", font=label_font, bg=cor_primaria, fg="white")
label_convidado.pack(pady=(10, 0))
var_convidado = tk.StringVar(inner_frame)
convidados = ["João", "Maria", "Pedro", "Ana", "Carlos"]
select_convidado = ttk.Combobox(inner_frame, textvariable=var_convidado, values=convidados, font=input_font, width=48)
select_convidado.pack(pady=(0, 10))
select_convidado.set("Selecione")

# Campo Nome do Local
label_nome_local = tk.Label(inner_frame, text="Nome do Local:", font=label_font, bg=cor_primaria, fg="white")
label_nome_local.pack(pady=(10, 0))
entry_nome_local = tk.Entry(inner_frame, width=input_width, font=input_font, relief="flat")
configurar_widget(entry_nome_local, "white", "#4A4A4A")
entry_nome_local.pack(pady=(0, 10))

# Campo Rua
label_rua = tk.Label(inner_frame, text="Rua:", font=label_font, bg=cor_primaria, fg="white")
label_rua.pack(pady=(10, 0))
entry_rua = tk.Entry(inner_frame, width=input_width, font=input_font, relief="flat")
configurar_widget(entry_rua, "white", "#4A4A4A")
entry_rua.pack(pady=(0, 10))

# Campo Número
label_numero = tk.Label(inner_frame, text="Número:", font=label_font, bg=cor_primaria, fg="white")
label_numero.pack(pady=(10, 0))
entry_numero = tk.Entry(inner_frame, width=input_width, font=input_font, relief="flat")
configurar_widget(entry_numero, "white", "#4A4A4A")
entry_numero.pack(pady=(0, 10))

# Label para selecionar o template
label_template = tk.Label(inner_frame, text="Selecione o template do convite:", font=label_font, bg=cor_primaria, fg="white")
label_template.pack(pady=(20, 0))

# Sessão das Imagens
frame_images = tk.Frame(inner_frame, bg=cor_primaria)
frame_images.pack(pady=20, anchor="center")

# Função para carregar e redimensionar a imagem
def carregar_imagem(caminho):
    img = Image.open(caminho)
    img = img.resize((300, 300), Image.LANCZOS)
    return ImageTk.PhotoImage(img)

# Caminhos das imagens (substitua pelos caminhos corretos das suas imagens)
caminho_imagem1 = "./templates/templates-backgrounds/background-1.jpg"
caminho_imagem2 = "./templates/templates-backgrounds/background-1.jpg"
caminho_imagem3 = "./templates/templates-backgrounds/background-1.jpg"

# Carregar as imagens
imagem1 = carregar_imagem(caminho_imagem1)
imagem2 = carregar_imagem(caminho_imagem2)
imagem3 = carregar_imagem(caminho_imagem3)

# Variável para rastrear a imagem selecionada
imagem_selecionada = None

# Função para selecionar a imagem e adicionar a borda
def selecionar_imagem(label):
    global imagem_selecionada
    # Remover a borda da imagem anteriormente selecionada
    if imagem_selecionada:
        imagem_selecionada.config(bd=0)
    # Adicionar a borda à imagem atual
    label.config(bd=5, relief="solid", highlightbackground="blue", highlightthickness=2)
    imagem_selecionada = label

# Adicionar as imagens e botões ao frame
# Imagem 1
frame1 = tk.Frame(frame_images, bg=cor_primaria)
frame1.pack(side=tk.LEFT, padx=10, anchor='center')
label_imagem1 = tk.Label(frame1, image=imagem1, bd=0)
label_imagem1.pack(pady=(0, 10))
botao1 = tk.Button(frame1, text="Selecionar", command=lambda: selecionar_imagem(label_imagem1), width=button_width, relief="flat")
configurar_widget(botao1, cor_terceira, "black")
botao1.pack()

# Imagem 2
frame2 = tk.Frame(frame_images, bg=cor_primaria)
frame2.pack(side=tk.LEFT, padx=10, anchor='center')
label_imagem2 = tk.Label(frame2, image=imagem2, bd=0)
label_imagem2.pack(pady=(0, 10))
botao2 = tk.Button(frame2, text="Selecionar", command=lambda: selecionar_imagem(label_imagem2), width=button_width, relief="flat")
configurar_widget(botao2, cor_terceira, "black")
botao2.pack()

# Imagem 3
frame3 = tk.Frame(frame_images, bg=cor_primaria)
frame3.pack(side=tk.LEFT, padx=10, anchor='center')
label_imagem3 = tk.Label(frame3, image=imagem3, bd=0)
label_imagem3.pack(pady=(0, 10))
botao3 = tk.Button(frame3, text="Selecionar", command=lambda: selecionar_imagem(label_imagem3), width=button_width, relief="flat")
configurar_widget(botao3, cor_terceira, "black")
botao3.pack()

# Botão de Envio (posicionado abaixo das imagens)
botao_enviar = tk.Button(inner_frame, text="Criar", command=enviar_dados, font=button_font, width=30, relief="flat")
configurar_widget(botao_enviar, cor_secundaria, "black")
botao_enviar.pack(pady=(30, 30))

# Executar o loop principal
root.mainloop()
