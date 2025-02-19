import scrapy

class QuotesToScrapeSpider(scrapy.Spider):
    # identidade
    name = 'frasebot'
    # Request
    def start_requests(self):
        # definir url(s) a varrer
        urls = ['https://www.goodreads.com/quotes?_gl=1*fty6y2*_ga*MTU1Mjg2NjQyOS4xNzM1ODI2MjU1*_ga_37GXT4VGQK*MTczOTk3MTY0Ni4xOS4xLjE3Mzk5NzYyODQuMC4wLjA./']

        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

     # response
    def parse(self, response):
        # aqui é onde deve processar o que é retornado da resposta 
       for elemento in response.xpath("//div[@class='quote']"):
           yield {
              'frase': elemento.xpath(".//div[@class='quoteText']/text()").get(),
              'autor': elemento.xpath(".//span[@class='authorOrTitle']/text()").get(),
              'tags': elemento.xpath(".//div[@class='greyText smallText left']/a/text()").getall() 
          }