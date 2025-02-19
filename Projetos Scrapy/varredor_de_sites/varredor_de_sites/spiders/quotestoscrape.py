import scrapy

class QuotesToScrapeSpider(scrapy.Spider):
    # identidade
    name = 'frasebot'
    # Request
    def start_requests(self):
        # definir url(s) a varrer
        urls = ['https://quotes.toscrape.com/']

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

     # response
    def parse(self, response):
        # aqui é onde deve processar o que é retornado da resposta 
        with open ('pagina.html', 'wb') as arquivo:
            arquivo.write(response.body)