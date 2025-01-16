from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome  import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pyautogui
from time import sleep

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




# 1 navegar até o site
driver.get('https://cursoautomacao.netlify.app/')
sleep(2)
# 2 encontrar e clicar no login
botao_login = driver.find_element(By.LINK_TEXT, 'Login')
botao_login.click()

# 3 encontrar e clicar no email
digitar_email = driver.find_element(By.ID, 'email')
sleep(2)

# 4 digitar email 
digitar_email.send_keys('giovani.eb3@gmail.com')

# 5 encontar e clicar na senha 
digitar_senha = driver.find_element(By.ID, 'senha')
sleep(2)
# 6 digitar senha 
digitar_senha.send_keys('12345678')

# 7 encontrar e clicar para enviar 
botao_enviar = driver.find_element(By.CLASS_NAME, 'btn.btn-primary')
botao_enviar.click()





input('')
driver.close()