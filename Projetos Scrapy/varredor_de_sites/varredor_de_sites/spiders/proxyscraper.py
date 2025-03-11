import scrapy

class ProxyScraperSpider(scrapy.Spider):

    # identidade
    name = 'proxyscraper'
    # request
    def start_requests(self):
        urls = ['https://free-proxy-list.net/web-proxy.html']
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

            # response
    def parse(self, response):
        for linha in response.xpath("//table[@class='table table-striped table-bordered']//tr"):
            yield {
                'proxy_name': linha.xpath('./td[1]/a/text()').get(),
                'domain': linha.xpath('./td[2]/text()').get(),
                'country': linha.xpath('./td[3]/text()').get(),
                'speed': linha.xpath('./td[4]/text()').get(),
                'popularity': linha.xpath('./td[5]/div/div/text()').get()
                
            }