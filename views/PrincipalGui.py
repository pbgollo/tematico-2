import tkinter as tk
from tkinter import messagebox
from controllers.EmailSenderController import EmailSenderController
from helpers.PersonalizarWidgets import PersonalizarWidgets
from helpers.CentralizarJanela import CentralizarJanela
from controllers.EventoController import EventoController
from database.db import SessionLocal  
import asyncio

class PrincipalView:
    def __init__(self, root, usuario):
        self.root = root
        self.usuario = usuario
        self.root.title("PlanGO")
        self.root.resizable(False, False)
        self.root.configure(bg="#70cfff")

        self.session = SessionLocal()
        
        self.evento_controller = EventoController(self.session)
        
        largura = 500
        altura = 600
        CentralizarJanela.centralizar(self.root, largura, altura)

        self.personalizar = PersonalizarWidgets()

        # Label "Meus Eventos"
        self.label_titulo = tk.Label(root, text="Meus Eventos")
        self.label_titulo.place(x=150, y=20)
        self.personalizar.configurar_giant_label(self.label_titulo, fg="white", bg="#70cfff")

        # Botão "Cadastrar novo evento"
        self.btn_cadastrar_evento = tk.Button(root, text="Cadastrar novo evento", command=lambda: self.cadastrar_evento(usuario))
        self.btn_cadastrar_evento.place(x=165, y=80, width=175)
        self.personalizar.configurar_button_azul(self.btn_cadastrar_evento)

        # Botão "Gerenciar Convidados"
        self.btn_gerenciar_convidados = tk.Button(root, text="Gerenciar Convidados", command=lambda: self.gerenciar_convidados(usuario))
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
        eventos = self.evento_controller.listar_eventos(self.usuario.id)

        if not eventos:
            messagebox.showinfo("Sem Eventos", "Nenhum evento encontrado!")
            return

        # Definir a largura fixa da coluna de informações (em pixels)
        largura_fixa_coluna_info = 250

        for index, evento in enumerate(eventos):
            num_convidados = self.evento_controller.contar_convidados(evento.id)
            # Crie o frame do evento e faça ele expandir horizontalmente
            frame_evento = tk.Frame(self.scrollable_frame, bg="white", relief="solid", bd=1)
            frame_evento.grid(row=index, column=0, pady=5, padx=0, sticky="ew")

            # Configurar a coluna do frame_evento para expandir
            frame_evento.columnconfigure(1, weight=1)

            # Imagem do evento (à esquerda)
            label_imagem = tk.Label(frame_evento, text="📅", font=("Arial", 24), bg="white", fg="orange")
            label_imagem.grid(row=0, column=0, padx=5, pady=5, sticky="w")

            # Informações do evento (nome, data e convidados)
            frame_info = tk.Frame(frame_evento, bg="white", width=largura_fixa_coluna_info)
            frame_info.grid(row=0, column=1, sticky="w")
            frame_info.columnconfigure(0, weight=1)

            # Labels com largura fixa
            label_nome_evento = tk.Label(frame_info, text=evento.nome, bg="white", anchor="w", width=largura_fixa_coluna_info // 10)
            label_nome_evento.grid(row=0, column=0, padx=5, sticky="w")
            self.personalizar.configurar_small_label(label_nome_evento, fg="black", bg="white")

            label_data_evento = tk.Label(frame_info, text=evento.data, bg="white", anchor="w", width=largura_fixa_coluna_info // 10)
            label_data_evento.grid(row=1, column=0, padx=5, sticky="w")
            self.personalizar.configurar_small_label(label_data_evento, fg="black", bg="white")

            label_convidados = tk.Label(frame_info, text=f"{num_convidados} convidados", bg="white", fg="black", anchor="w", width=largura_fixa_coluna_info // 10)
            label_convidados.grid(row=2, column=0, padx=5, sticky="w")
            self.personalizar.configurar_small_label(label_convidados, fg="#878484", bg="white")

            # Frame para os botões (à direita)
            frame_botoes = tk.Frame(frame_evento, bg="white")
            frame_botoes.grid(row=0, column=2, sticky="e", padx=5)

            # Botão de excluir
            btn_editar = tk.Button(frame_botoes, text="Excluir", command=lambda e=evento: self.excluir_evento(e))
            btn_editar.grid(row=0, column=0, padx=5, pady=2, sticky="e")
            self.personalizar.configurar_button_azul(btn_editar)

            # Botão de enviar convites
            btn_enviar_convites = tk.Button(frame_botoes, text="Enviar convites", command=lambda e=evento: self.enviar_convites(e))
            btn_enviar_convites.grid(row=1, column=0, padx=5, pady=2, sticky="e")
            self.personalizar.configurar_button_amarelo(btn_enviar_convites)

    def cadastrar_evento(self, usuario):
        self.root.withdraw()
        evento_root = tk.Toplevel(self.root)
        
        def reabrir_principal():
            evento_root.destroy()
            self.root.deiconify() 
        
        from views.EventoGui import EventoView
        EventoView(evento_root, usuario, reabrir_principal)

    def gerenciar_convidados(self, usuario):
        self.root.withdraw()
        convidados_root = tk.Toplevel(self.root)
        
        def reabrir_principal():
            convidados_root.destroy()
            self.root.deiconify() 
    
        from views.ConvidadoGui import ConvidadoView
        ConvidadoView(convidados_root, usuario, reabrir_principal)

    def excluir_evento(self, evento):
        resultado = self.evento_controller.excluir_evento(evento.id)
        
        if resultado["success"]:
            self.listar_eventos()
            
            messagebox.showinfo("Sucesso", "Evento excluído com sucesso!")
        else:
            messagebox.showerror("Erro", resultado["message"])


    def enviar_convites(self, evento):
        convidados = self.evento_controller.listar_convidados_por_evento(evento.id)

        if not convidados:
            messagebox.showinfo("Sem Convidados", "Nenhum convidado encontrado para este evento.")
            return

        template_escolhido = evento.template_id or 1

        for convidado in convidados:
            nome_convidado = convidado["nome"]
            email_convidado = convidado["email"]

            variaveis_html = {
                'titulo': nome_convidado,
                'nome_evento': evento.nome,
                'mensagem': f"Você está convidado para {evento.nome}!",
                'data': evento.data,
                'hora': evento.hora,
                'local': evento.local,
                'endereco': evento.endereco,
                'comidas': evento.comida or "Não especificado",
                'bebidas': evento.bebida or "Não especificado",
            }

            infos = {
                "template_escolhido": template_escolhido,
                "destinatario": email_convidado,
                "numero_celular": self.usuario.telefone,
                "assunto": f"Convite: {evento.nome}",
                "mensagem_texto": f"Você está convidado para {evento.nome}. Veja o convite em anexo.",
                "imagem_output": f"assets/convite_{evento.id}_{nome_convidado}.png",
            }

            try:
                convite = EmailSenderController(variaveis_html, template_escolhido)
                asyncio.run(convite.criar_e_enviar_convite(infos))
                print(f"Convite enviado para {nome_convidado} <{email_convidado}>")
            except Exception as e:
                print(f"Erro ao enviar convite para {nome_convidado} <{email_convidado}>: {e}")
                messagebox.showerror("Erro", f"Erro ao enviar convite para {nome_convidado} <{email_convidado}>: {e}")

        messagebox.showinfo("Convites Enviados", "Convites enviados para todos os convidados com sucesso!")








    def on_close(self):
        self.session.close()
        self.root.destroy()
