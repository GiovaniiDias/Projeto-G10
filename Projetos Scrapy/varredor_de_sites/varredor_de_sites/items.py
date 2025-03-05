# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Join


def tira_espaços_em_branco(valor):
    return valor.strip()

def processar_caracteres_especiais(valor):
    return valor.replace(u"201c",'').replaceu(u"\u201d",'')
   


class CitacaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    frase = scrapy.Field(
        input_processor=MapCompose(tira_espaços_em_branco, processar_caracteres_especiais ),
        output_processor=TakeFirst()

    )
    autor = scrapy.Field(
        output_processor=TakeFirst()
    )
    tags = scrapy.Field(
        output_processor=Join(',')
    )

    pass
