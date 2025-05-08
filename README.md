# jobs-crawler

Trabalho desenvolvido para disciplina de Tópicos Especiais em Gerência de dados.
Primeiramente, foi desenvolvido um Crawler que salva em um arquivo .txt os links de vagas de emprego em T.I do site https://www.vagas.com.br/ , utilizando BeautifulSoup.
Após, foi desenvolvido uma Spider (utilizando Scrapy), que raspa os dados de cada vaga, passando por todos os links coletados na etapa anterior. 

- jobs-crawler/jobs/url_vagas.txt é o arquivo com os links das vagas, para a data de coleta.
- jobs-crawler/jobs.json é o arquivo resultante do processo de raspagem dos dados.
