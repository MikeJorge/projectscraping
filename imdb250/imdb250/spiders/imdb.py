import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    start_urls = ['https://www.imdb.com/title/tt15496380/fullcredits/?ref_=tt_ov_wr#writer']

    def parse(self, response):
        for elenco in response.css('.primary_photo+ td , .odd:nth-child(2) a'):
            yield {
                'personagem': response.css('.character , .character a').get(),
                'elenco': response.css(' #director+ .simpleCreditsTable a , .even td').get()
            }