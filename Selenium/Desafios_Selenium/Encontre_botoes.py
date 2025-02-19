from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome  import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def iniciar_driver():

    chrome_options = Options()
    #fonte de opções de switches https://peter.sh/experients/chromium-command-line-switches/

    arguments = ['--lang=ptBR', '--window-size=800,600', '--incognito']

    '''
    Common arguments
    --start-maximized # indica maximizado
    --lang=pt-BR #Define o idioma
    --incognito # Modo anonimo
    --window-size=800,800 #define a resolução da janela
    --headless # Roda em segundo plano (com a janela fechada)
    --disable-notifications # desabilita notificações
    --disable-gpu # desabilita as renderizações com gpu

    '''
    for argument in arguments:
        chrome_options.add_argument(argument)

    caminho_padrao_para_download = 'E:\\Storege\\Desktop'

    #lista de opções experimentais https://chromium.googlesource.com/chromium/src/+/32352ad08ee673a4d43e8593ce988b224f6482d3/chrome/common/pref_names.cc?_gl=1*13aal8q*_ga*MTI1NTU4ODE5OC4xNzM2NDQzMzk5*_ga_37GXT4VGQK*MTczNjc3NTQ5NS43LjEuMTczNjc3NTUyOC4wLjAuMA..
    chrome_options.add_experimental_option('prefs', { 'download.default_directory': caminho_padrao_para_download,
    #atualiza o diretorio para o diretorio acima
    'download.directory_upgrade' : True,
    #setar se o vagador deve pedir ou não para fazer download
        'dowload.prompt_for_download': False,
        "profile.default_content_setting_values.notifications": 2, #desabilita notificações
        #allow multiple downloads
        "profile.default_content_setting_values.automatic_downloads": 1,
        })

    driver = webdriver.Chrome(options=chrome_options)
    return driver

driver = iniciar_driver()

driver.get('https://cursoautomacao.netlify.app/desafios')

botao1 = driver.find_element(By.ID,'btn1')
botao2 = driver.find_element(By.CLASS_NAME, 'btn2.btn.btn-dark')   # tirar os espaços e colocar ponto entre elas
botao3 = driver.find_element(By.CLASS_NAME, 'btn2.btn.btn-warning')

if botao1.is_enabled():
    print('Botão 1 Habilitado')
    
if botao1.is_enabled()== False:
    print('Botão 1 esta Desabilitado')

if botao2.is_enabled():
    print('Botão 2 Habilitado')
if botao2.is_enabled()== False:
    print('Botão 2 Desabilitado')

if botao2.is_enabled():
    print('Botão 3 Habilitado')
if botao2.is_enabled()== False:
    print('Botão 3 Desabilitado')



input('')
driver.close()