import requests
print()


retorno = requests.get('https://leonnecred.sistemayuppie.com.br/public/proposta/update/id/13917') 
"""
aqui eu faço um 'pedido' pro servidor me retornar 
o que está nesse endereço de link informado
"""

print('Status: ', retorno.status_code)
'''
Esse status code me retorna o status da solicitação
familia 100 é informação
familia 200 é sucesso
familia 300 é sobre redirecionamentos
familia 400 é erro do cliente
familia 500 é erro do servidor 
'''
print('Header: ', retorno.headers)
'''
Aqui mostra todas as informações sobre o servidor
'''
print('Conteudo: ', retorno.content)
'''
aqui está todo o conteudo html da página
'''

