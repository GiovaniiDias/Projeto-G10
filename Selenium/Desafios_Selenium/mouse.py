from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome  import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
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

#acessando o site
driver.get('https://cursoautomacao.netlify.app/exemplo_chains')

# clicando no botão

botao_direito=driver.find_element(By.ID,'botao-direito')
chain=ActionChains(driver)
chain.context_click(botao_direito).pause(2).send_keys(Keys.DOWN).pause(2).send_keys(Keys.DOWN).pause(2).click().perform()




input('')
driver.close()