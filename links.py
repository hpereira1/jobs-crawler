from bs4 import BeautifulSoup

# script que armazena os links das vagas de emprego da pagina html em um arquivo de texto
html_file = '/home/pero/PycharmProjects/webscrapyjobs/jobs/Vagas de emprego de Informática_T.I. _ Vagas.com.html'
output_file = 'jobs/urls_vagas.txt'

with open(html_file, 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

links = soup.find_all('a', class_='link-detalhes-vaga')

urls = [link['href'] for link in links if 'href' in link.attrs]

with open(output_file, 'w', encoding='utf-8') as file:
    for url in urls:
        file.write(f'{url}\n')

print(f'URLs extraídos e salvos em {output_file}')
