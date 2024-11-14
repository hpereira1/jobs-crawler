from http.client import responses

import scrapy
from jobs.items import JobsItem
from datetime import date

class VagasSpider(scrapy.Spider):
    name = 'vagas'

    start_urls = ['https://www.vagas.com.br/vagas-de-desenvolvedor?']
    total_jobs = []
    def parse(self, response):
        job_table = response.xpath('/html/body/div[1]/div[3]/div/div/div[2]/section/section/div/ul')
        for job in job_table.xpath('.//li'):
            link = job.xpath('.//a/@href').get()
            if link:
                yield response.follow(link,self.parse_job)


    def parse_job(self,response):
        job = JobsItem()
        job['title'] = response.css('.job-shortdescription__title::text').get().strip()
        job['level'] = response.css('.job-hierarchylist__item > span:nth-child(1)::text').get().strip()
        job['company'] = response.css('.job-shortdescription__company::text').get().strip()
        job['location'] = response.css('.info-localizacao::text').get().strip()
        job['description'] = response.css('.info-modelo-contratual::text').get().strip()
        published_text = ''.join([text.strip() for text in response.xpath('/html/body/div[1]/section[1]/div/div[1]/ul/li[1]//text()').getall() if text.strip()])
        date_str = published_text.replace('Publicada em ', '')
        job['published_date'] = date_str
        job['scraping_date'] = date.today().strftime('%d/%m/%Y')
        job['link'] = response.url

        yield job