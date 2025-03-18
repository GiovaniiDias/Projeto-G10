import scrapy
from datetime import datetime
from utils.email_sender import Emailer


class PriceScraperSpider(scrapy.Spider):
    # identidade
    name = 'dolarbot'
    # Request

    def start_requests(self):
        urls = ['https://www.investing.com/currencies/usd-brl']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Response
    def parse(self, response):
        dolar = response.xpath(
            "//span[@data-test='instrument-price-last']/text()")[0].get()

        if float(dolar) > 5.70:
            email = Emailer('giovani.eb3@gmail.com',
                            'cwsn sypq romc wmwr')
            lista_de_contatos = ['giovani.eb3@gmail.com']
            email.definir_conteudo('Variação do Dolár', 'giovani.eb3@gmail.com', lista_de_contatos,f'O dólar acabou de subir para {dolar}, favor verificar se agora é um bom momento para comprar dólar.')

            email.enviar_email(30)
