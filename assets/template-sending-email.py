import base64
from pyppeteer import launch
import asyncio
import smtplib
from email.message import EmailMessage
import mimetypes
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
background_1_path = os.path.join(base_dir, 'templates-backgrounds', 'background-1.jpg')
template_1_path = os.path.join(base_dir, 'templates', 'template-1.html')

background_2_path = os.path.join(base_dir, 'templates-backgrounds', 'background-2.jpg')
template_2_path = os.path.join(base_dir, 'templates', 'template-2.html')

# Função para converter imagem para Base64
def converter_imagem_para_base64(caminho_imagem):
    with open(caminho_imagem, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Função para gerar a imagem do HTML
async def gerar_imagem_do_html(arquivo_html, output_image_path, variaveis, caminho_imagem):
    # Caminho para o Google Chrome instalado no sistema
    caminho_chrome = 'C:/Program Files/Google/Chrome/Application/chrome.exe'

    # Ler o conteúdo do template HTML
    with open(arquivo_html, 'r', encoding='utf-8') as file:
        template = file.read()

    # Converter a imagem para Base64
    imagem_base64 = converter_imagem_para_base64(caminho_imagem)

    # Substituir os placeholders no HTML com os valores dinâmicos
    for chave, valor in variaveis.items():
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

# Função para enviar o e-mail com a imagem gerada como anexo
def enviar_email_com_imagem(destinatario, assunto, mensagem_texto, caminho_imagem):
    remetente = "lucas.bessegato96@gmail.com"  # Substitua pelo seu e-mail
    senha = "hqob cpdo enth etsj"        # Substitua pela sua senha de app

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

# Configurações para geração de imagem e envio de e-mail
variaveis = {
    'titulo': 'Convite de Aniversário',
    'mensagem': 'Você está convidado para o aniversário de Cristina!',
    'nome_aniversariante': 'Besse besse aea'
}
arquivo_html = template_2_path
imagem_output = 'convite_aniversario.png'
destinatario = "lucas.bessegato98@gmail.com"
assunto = "Convite de Aniversário"
mensagem_texto = "Você está convidado para a festa! Veja o convite em anexo."


# Geração da imagem e envio do e-mail em sequência
async def main():
    await gerar_imagem_do_html(arquivo_html, imagem_output, variaveis, background_2_path)
    enviar_email_com_imagem(destinatario, assunto, mensagem_texto, imagem_output)

# Executar as funções assíncronas e sincronas em sequência
asyncio.run(main())
