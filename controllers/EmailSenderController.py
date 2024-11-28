import base64
from urllib.parse import quote
from pyppeteer import launch
import asyncio
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import mimetypes
import os

class EmailSenderController:
    def __init__(self, variaveis_html, template_escolhido):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.templates = {
            1: {
                "background": os.path.join(self.base_dir, 'templates-backgrounds', 'background-1.jpg'),
                "template": os.path.join(self.base_dir, 'templates', 'template-1.html')
            },
            2: {
                "background": os.path.join(self.base_dir, 'templates-backgrounds', 'background-2.jpg'),
                "template": os.path.join(self.base_dir, 'templates', 'template-2.html')
            },
            3: {
                "background": os.path.join(self.base_dir, 'templates-backgrounds', 'background-3.jpg'),
                "template": os.path.join(self.base_dir, 'templates', 'template-3.html')
            }
        }
        self.variaveis_html = variaveis_html
        self.template_escolhido = self.templates.get(template_escolhido, self.templates[1])

    @staticmethod
    def converter_imagem_para_base64(caminho_imagem):
        """Converte uma imagem para Base64."""
        with open(caminho_imagem, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')

    async def gerar_imagem_do_html(self, output_image_path):
        """Gera uma imagem do HTML preenchido."""
        caminho_chrome = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
        arquivo_html = self.template_escolhido["template"]
        caminho_imagem = self.template_escolhido["background"]

        # Ler o conteúdo do template HTML
        with open(arquivo_html, 'r', encoding='utf-8') as file:
            template = file.read()

        # Converter a imagem para Base64
        imagem_base64 = self.converter_imagem_para_base64(caminho_imagem)

        # Substituir os placeholders no HTML com os valores dinâmicos
        for chave, valor in self.variaveis_html.items():
            template = template.replace(f'{{{{{chave}}}}}', valor)

        # Substituir o placeholder da imagem base64 no HTML
        template = template.replace('{{imagem_base64}}', f'data:image/jpeg;base64,{imagem_base64}')

        # Lançar o Google Chrome instalado no sistema
        browser = await launch(executablePath=caminho_chrome)
        page = await browser.newPage()

        # Carregar o conteúdo HTML na página
        await page.setContent(template)

        # Capturar a screenshot da página
        await page.screenshot({'path': output_image_path, 'fullPage': True})

        # Fechar o navegador
        await browser.close()
        print(f"Imagem salva em: {output_image_path}")

    def enviar_email_com_imagem(self, infos):
        """Envia um e-mail com a imagem gerada como anexo."""
        load_dotenv()
        remetente = os.getenv('GMAIL_ACCOUNT')
        senha = os.getenv('GMAIL_APP_PASSWORD')

        # Verificar se o arquivo de imagem existe
        if not os.path.isfile(infos["imagem_output"]):
            print(f"Erro: O arquivo '{infos['imagem_output']}' não foi encontrado.")
            return

        # Configuração do servidor SMTP do Gmail
        servidor = "smtp.gmail.com"
        porta = 587

        # Formatar o número de celular
        numero_celular_formatado = f"55{infos['numero_celular']}"

        # Criar o link do WhatsApp
        mensagem_whatsapp = f"Estou confirmando minha presença no evento {self.variaveis_html["titulo"]}, agradeço o convite!"
        mensagem_codificada = quote(mensagem_whatsapp)
        link_whatsapp = f"https://wa.me/{numero_celular_formatado}?text={mensagem_codificada}"

        # Criar o e-mail
        msg = EmailMessage()
        msg["From"] = remetente
        msg["To"] = infos["destinatario"]
        msg["Subject"] = infos["assunto"]

        mensagem_html = f"""
        <html>
            <body>
                <p>{infos['mensagem_texto']}</p>
                <p>Clique no botão abaixo para confirmar sua presença pelo WhatsApp:</p>
                <a href="{link_whatsapp}" 
                   style="display: inline-block; 
                          padding: 10px 20px; 
                          font-size: 16px; 
                          color: #ffffff; 
                          background-color: #6565ff; 
                          text-decoration: none; 
                          border-radius: 5px;">
                   Confirmar Presença
                </a>
            </body>
        </html>
        """
        msg.add_alternative(mensagem_html, subtype='html')

        # Adicionar a imagem como anexo
        with open(infos["imagem_output"], "rb") as img_file:
            img_data = img_file.read()
            img_type, _ = mimetypes.guess_type(infos["imagem_output"])
            img_type = img_type or "image/png"
            msg.add_attachment(img_data, maintype="image", subtype=img_type.split('/')[1], filename=os.path.basename(infos["imagem_output"]))

        # Enviar o e-mail
        try:
            with smtplib.SMTP(servidor, porta) as smtp:
                smtp.starttls()  # Conectar ao servidor usando TLS
                smtp.login(remetente, senha)  # Fazer login
                smtp.send_message(msg)  # Enviar o e-mail
                print("E-mail enviado com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar o e-mail: {e}")

    async def criar_e_enviar_convite(self, infos):
        """Executa a geração do convite e o envio do e-mail."""
        await self.gerar_imagem_do_html(infos["imagem_output"])
        self.enviar_email_com_imagem(infos)


# Exemplo de uso
variaveis_html = {
    'titulo': 'Aniversário do Gollo',
    'mensagem': 'Você está convidado para o aniversário do Gollo!',
    'data': '20/10/2025',
    'hora': '18',
    'local': 'Casa das pedras',
    'endereco': 'Rua doutor júlio rosa cruz, 692',
    'comidas': 'Aliquam, odit quas iusto quasi natus perspiciatis ipsum animi, aut quos facere mollitia omnis, quam nulla maiores. Aliquam quaerat doloremque qui neque!',
    'bebidas': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquam, odit quas iusto quasi natus perspiciatis ipsum animi.'
}

infos = {
    "template_escolhido": 3,
    "destinatario": "pedrobgollo@gmail.com",
    "numero_celular": "54999617064",
    "assunto": "Convite de Aniversário",
    "mensagem_texto": "Você está convidado para a festa! Veja o convite em anexo.",
    "imagem_output": "convite_aniversario.png"
}

convite = EmailSenderController(variaveis_html, infos["template_escolhido"])

# Chamar as funções
asyncio.run(convite.criar_e_enviar_convite(infos))
