import base64
from pyppeteer import launch
import asyncio
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import mimetypes
import os


class ConvitePersonalizado:
    def __init__(self, variaveis, template_escolhido):
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
        self.variaveis = variaveis
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
        for chave, valor in self.variaveis.items():
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

    def enviar_email_com_imagem(self, destinatario, assunto, mensagem_texto, caminho_imagem):
        """Envia um e-mail com a imagem gerada como anexo."""
        load_dotenv()
        remetente = os.getenv('GMAIL_ACCOUNT')
        senha = os.getenv('GMAIL_APP_PASSWORD')

        # Verificar se o arquivo de imagem existe
        if not os.path.isfile(caminho_imagem):
            print(f"Erro: O arquivo '{caminho_imagem}' não foi encontrado.")
            return

        # Configuração do servidor SMTP do Gmail
        servidor = "smtp.gmail.com"
        porta = 587

        # Criar o e-mail
        msg = EmailMessage()
        msg["From"] = remetente
        msg["To"] = destinatario
        msg["Subject"] = assunto

        # Adicionar o texto do e-mail
        msg.set_content(mensagem_texto)

        # Adicionar a imagem como anexo
        with open(caminho_imagem, "rb") as img_file:
            img_data = img_file.read()
            img_type, _ = mimetypes.guess_type(caminho_imagem)
            img_type = img_type or "image/png"
            msg.add_attachment(img_data, maintype="image", subtype=img_type.split('/')[1], filename=os.path.basename(caminho_imagem))

        # Enviar o e-mail
        try:
            with smtplib.SMTP(servidor, porta) as smtp:
                smtp.starttls()  # Conectar ao servidor usando TLS
                smtp.login(remetente, senha)  # Fazer login
                smtp.send_message(msg)  # Enviar o e-mail
                print("E-mail enviado com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar o e-mail: {e}")

    async def criar_e_enviar_convite(self, destinatario, assunto, mensagem_texto, output_image_path):
        """Executa a geração do convite e o envio do e-mail."""
        await self.gerar_imagem_do_html(output_image_path)
        self.enviar_email_com_imagem(destinatario, assunto, mensagem_texto, output_image_path)


# Exemplo de uso
variaveis = {
    'titulo': 'Convite de Aniversário',
    'mensagem': 'Você está convidado para o aniversário de Cristina!',
    'data': '20/10/2025',
    'hora': '18',
    'local': 'Casa das pedras',
    'endereco': 'Rua doutor júlio rosa cruz, 692',
    'comidas': 'Aliquam, odit quas iusto quasi natus perspiciatis ipsum animi, aut quos facere mollitia omnis, quam nulla maiores. Aliquam quaerat doloremque qui neque!',
    'bebidas': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquam, odit quas iusto quasi natus perspiciatis ipsum animi.'
}
template_escolhido = 3
destinatario = "lucas.bessegato98@gmail.com"
assunto = "Convite de Aniversário"
mensagem_texto = "Você está convidado para a festa! Veja o convite em anexo."
imagem_output = 'convite_aniversario.png'

convite = ConvitePersonalizado(variaveis, template_escolhido)

# Chamar as funções
asyncio.run(convite.criar_e_enviar_convite(destinatario, assunto, mensagem_texto, imagem_output))
