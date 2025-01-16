from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome  import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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
driver.get('https://cursoautomacao.netlify.app/desafios')

# salvando essa pagina como a janela inicial
janela_inicial=driver.current_window_handle

# rolando até o fim da pagina 
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
sleep(1)

# clicando no botão abrir janela
botao_nova_janela=driver.find_element(By.XPATH,"//button[text()='Abrir nova janela']")
botao_nova_janela.click()
# se o .click não funcionar pode usar essa opção tbm
# driver.execute_script('arguments[0].click()',botao_nova_janela)
sleep(1)

#verificando as janelas atuais
janelas=driver.window_handles
for janela in janelas:
    print(janelas)
    if janela not in janela_inicial:
        #alterar de janela 
        driver.switch_to.window(janela)
        sleep(1)
        campo_pesquisa=driver.find_element(By.ID,'opiniao_sobre_curso')
        campo_pesquisa.send_keys('texto qualque escolhido para digitar na caixa.')
        sleep(1)
        botao_pesquisa=driver.find_element(By.ID,'fazer_pesquisa')
        botao_pesquisa.click()
        sleep(1)
        driver.close()
        sleep(1)
        #voltando para a janela inicial
driver.switch_to.window(janela_inicial)
sleep(1)
nova_msg=driver.find_element(By.ID,'campo_desafio7')
nova_msg.send_keys('textinho para finalizar')
sleep(2)
driver.close()

# pode ser usado para abas tbm.

input('')
driver.close()