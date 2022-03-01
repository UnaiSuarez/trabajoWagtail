from bs4 import BeautifulSoup
import requests
import random

contador = 0
title=[]

for x in range(10):
    page_link = 'https://as.com/meristation/juegos/listado/{}/'.format(x)
    page_response = requests.get(page_link, timeout=5)
    soup  = BeautifulSoup(page_response.content, "html.parser")

    for link in soup.select('div[class=mod-ga-det]'):
        precioAleatorio = random.randint(0, 100)
        if link.find('div', class_='ga-art').find('div', class_='rv-sc sc-m') == None:
            rankAleatorio = random.randint(0,10)
        else:
            rankAleatorio = link.find('div', class_='ga-art').find('div', class_='rv-sc sc-m').text

        ranking = {
            'titulo': link.find('div', class_='ga-inf').find('h2', class_='ga-tl').text,
            'precio': precioAleatorio,
            'Rating' : rankAleatorio,
            'plataformas': link.find('div', class_="ga-inf").find('ul', class_='rel-tags').text,
            'categoria': link.find('div', class_ ='ga-inf').find('div', class_='ga-plot').text,
            'genero': link.find('div', class_ ='ga-inf').find('ul', class_='ga-gen').text,
            'link': link.find('div', class_='ga-inf').find('h2', class_='ga-tl').find('a')['href'],
            'img': link.find('div', class_='ga-art').find('img')['src']
            # 'URL' : link.find('div', class_="di-ib clearfix").find('a')['href'],

        }
        title.append(ranking)
        contador = contador + 1
    print(contador)
    def write_csv(items, path):
        # Open the file in write mode
        with open(path, 'w', encoding='utf-8') as f:
            # Return if there's nothing to write
            if len(items) == 0:
                return

            # Write the headers in the first line
            headers = list(items[0].keys())
            f.write(','.join(headers) + '\n')

            # Write one item per line
            for item in items:
                values = []
                for header in headers:
                    registros = item.get(header, "")
                    values.append(str(registros))
                f.write(','.join(values) + "\n")

write_csv(title, "juegos.csv")