import smtplib
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from pyppeteer import launch
import asyncio

def converter_imagem_para_base64(caminho_imagem):
    with open(caminho_imagem, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

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
    

def enviar_email_com_imagem(destinatario, assunto, caminho_imagem):
    remetente_email = 'lucas.bessegato96@gmail.com'  # Seu e-mail do Gmail
    senha_app = 'amqrpiedcfsqoif'  # Cole aqui a senha de app gerada no Gmail

    # Criar o objeto do e-mail
    msg = MIMEMultipart()
    msg['Subject'] = assunto
    msg['From'] = remetente_email
    msg['To'] = destinatario

    # Anexar a imagem ao e-mail
    with open(caminho_imagem, 'rb') as img_file:
        img = MIMEImage(img_file.read())
        img.add_header('Content-Disposition', 'attachment', filename='convite_aniversario.png')
        msg.attach(img)

    try:
        # Conectar ao servidor SMTP do Gmail
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remetente_email, senha_app)
        servidor.sendmail(remetente_email, destinatario, msg.as_string())
        servidor.quit()
        print(f"E-mail enviado com sucesso para {destinatario}!")
    except Exception as e:
        print(f"Falha ao enviar e-mail: {str(e)}")

# Exemplo de uso:
variaveis = {
    'titulo': 'Convite de Aniversário',
    'mensagem': 'Você está convidado para o aniversário de Cristina!',
    'nome_aniversariante': 'Besse besse aea'
}

# Caminho da imagem local que será convertida para Base64
caminho_imagem_local = 'background-1.jpg'

# Gerar a imagem do HTML usando Pyppeteer
arquivo_html = 'template-aniversario.html'
imagem_output = 'convite_aniversario.png'
asyncio.run(gerar_imagem_do_html(arquivo_html, imagem_output, variaveis, caminho_imagem_local))

# Enviar o e-mail com a imagem como anexo
enviar_email_com_imagem('lucas.bessegato98@gmail.com', 'Seu Convite de Aniversário', imagem_output)
