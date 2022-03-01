import requests
from bs4 import BeautifulSoup
print()

# recebo da página
retorno = requests.get('https://leonnecred.sistemayuppie.com.br/public/proposta/update/id/13917') 
# separo o conteudo da página
conteudo = retorno.content
# transformo o conteudo num objeto BeautifulSoup
site = BeautifulSoup(conteudo, 'html.parser')
print(site.prettify)


