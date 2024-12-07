from datetime import date
import scrapy
from jobs.items import JobsItem
from scrapy.http import Request

class VagasSpider(scrapy.Spider):
    name = 'vagas'

    links_file = "/home/pero/PycharmProjects/webscrapyjobs/jobs/jobs/urls_vagas.txt"

    # Inicia a requisição para cada link de vaga, passando parse como callback
    def start_requests(self):
        try:
            with open(self.links_file, "r", encoding="utf-8") as f:
                links = f.readlines()
        except FileNotFoundError:
            self.logger.error("file {self.links_file} not found")
            return

        for link in links:
            link = link.strip()
            if link:
                yield Request(link, callback=self.parse)

    def parse(self, response):
        # Extrai as informações detalhadas de cada vaga
        job = JobsItem()
        job['title'] = response.css('.job-shortdescription__title::text').get(default='').strip()
        job['seniority'] = response.css('.job-hierarchylist__item > span:nth-child(1)::text').get(default='').strip()
        job['company'] = response.css('.job-shortdescription__company::text').get(default='').strip()
        job['location'] = response.css('.info-localizacao::text').get(default='').strip()
        job['description'] = response.css('.info-modelo-contratual::text').get(default='').strip()

        # Extrai a data de publicação e formata
        published_text = ''.join([text.strip() for text in response.xpath(
            '/html/body/div[1]/section[1]/div/div[1]/ul/li[1]//text()').getall() if text.strip()])
        date_str = published_text.replace('Publicada em ', '')
        job['published_date'] = date_str

        # Data de scraping
        job['scraping_date'] = date.today().strftime('%d/%m/%Y')

        # Link para a vaga
        job['link'] = response.url

        yield job