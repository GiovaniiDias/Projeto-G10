from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome  import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

def iniciar_driver():

    chrome_options = Options()
    #fonte de opções de switches https://peter.sh/experients/chromium-command-line-switches/

    arguments = ['--lang=ptBR', '--window-size=800,800', '--incognito']

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
driver.get('https://www.instagram.com/')
sleep(2)
# entrar no insta
usuario=driver.find_element(By.XPATH,"//input[@name='username']")
usuario.send_keys('+5551983405464')
sleep(1)
# digitar usuario e senha 
senha=driver.find_element(By.XPATH,"//input[@aria-label='Senha']")
senha.send_keys('GDA101992')
sleep(1)
# entrar
botao_entrar=driver.find_element(By.XPATH,"//div[text()='Entrar']")
botao_entrar.click()
sleep(10)

while True:
# procurar a pagina desejada
    driver.get('https://www.instagram.com/devaprender/')
    sleep(2)
    # clicar na ultima postagem

    ultima_postagem=driver.find_element(By.XPATH,"//div[@class='_aagw']")
    ultima_postagem.click()
    sleep(2)


    # realizar a verificação se foi curtida, caso não , curtir e comentar. 
    try:
            verifica_curtida = driver.find_element(By.XPATH,'//section//div[@role="button"]//*[@aria-label="Curtir"]')
    except:
            print('A ultima postagem já foi curtida.')
            sleep(86400)
    else:
            botao_curtir = driver.find_elements(By.XPATH,
                                                '//article[@role="presentation"]//section//div[@role="button"]')
            sleep(5)
            driver.execute_script('arguments[0].click()', botao_curtir[0])
            print('Feito! Ultima postagem curtida.')

            # aguardar 24h e retomar o processo 
    sleep(84400)

input('')
driver.close()