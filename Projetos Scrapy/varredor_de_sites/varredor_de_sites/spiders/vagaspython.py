
# https://br.indeed.com/jobs?q=python&l&from=searchOnHP&vjk=ef1205fc3520566b
import scrapy
from time import sleep


class IndeedPythonSpider(scrapy.Spider):
    # identidade
    name = 'vagaspythonbot'
    # request

    def start_requests(self):
        urls = [
            'https://br.indeed.com/jobs?q=python&vjk=f5b54117a62f77a6']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    # response

    def parse(self, response):
        # varrer cada grupo de informação e seus detalhes
        for item in response.xpath("//td[@class='resultContent css-lf1alc eu4oa1w0']"):
            yield {
                'cargo': item.xpath(".//span[1]/text()").get(),
                'nome empresa': item.xpath(".//span[@data-testid='company-name']/text()").get(),
                'local': item.xpath(".///div[@data-testid='text-location']/text()").get(),
                'link': 'https://br.indeed.com' + item.xpath(".//a/@href").get()
            }
        try:
            link_proxima_pagina = response.xpath("//a[@data-testid='pagination-page-next']/@href").get()
            print('#'*10)
            print(link_proxima_pagina)
            print('#'*10)

            link_completo = 'https://br.indeed.com' + link_proxima_pagina
            print('#'*10)
            print(link_completo)
            print('#'*10)
            yield scrapy.Request(url=link_completo, callback=self.parse)

        except Exception as error:
            print(error)
            print('Chegamos na ultima pagina')
