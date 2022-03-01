from bs4.element import ProcessingInstruction
import requests
from bs4 import BeautifulSoup
import pandas
print()
listadenoticias = []
# recebo da página
retorno = requests.get('https://g1.globo.com/') 
# separo o conteudo da página
conteudo = retorno.content
# transformo o conteudo num objeto BeautifulSoup
site = BeautifulSoup(conteudo, 'html.parser')
# o método find encontra um local no html, recebendo como paramentros: 1: tag, 2: atributo
posts = site.findAll('div', attrs={'class': 'feed-post-body'})
for post in posts:
    # aqui eu refino minha busca, indo atrás apenas da tag do titulo
    titulo = post.find('a', attrs={'class':'feed-post-link'})
    # aqui eu pego o subtitulo
    sub = post.find('a', attrs={'class': 'bstn-relatedtext'})
    # aqui eu printo apenas o texto dos resultados
    # print(titulo.text)
    # print(titulo['href']) # da pra acessar os atributos da tag pelo index, como se fosse um dict
    if sub:
        listadenoticias.append([titulo.text, sub.text, titulo['href']])
    else:
        listadenoticias.append([titulo.text, '', titulo['href']])
# Esse DataFrame do pandas, transforma o conteudo em colunas
news = pandas.DataFrame(listadenoticias, columns=['Título', 'Subtítulo', 'Links'])
# e esse método transforma o arquivo em excel
news.to_excel('Noticias.xlsx', index=False)