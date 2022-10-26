"""
# Automação de pesquisa no googlemaps
# criar chave api
# habilitar serviços places
## ~R$ 100,00 por mil. $ 200 por mês gratuitamente. A partir de 100 mil
## requisições por mês ~ $R 80,50
by Wesin Ribeiro
"""

# importar bibliotecas
import googlemaps
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
import time

# criar cliente para consulta a api google maps
gmaps = googlemaps.Client(key='sua chave aqui')

# pesquisar por assunto
dados_pesquisa = []
places = gmaps.places("Restaurantes em brasília")

# obter dados dos lugares
for i in range(5):
    time.sleep(2)
    for place in places['results']:
        request = gmaps.place(place['place_id'])
        fone = request['result'].get('formatted_phone_number', 'vazio')
        votos = request['result'].get('user_ratings_total', 'vazio')
        dados_pesquisa.append(
            {
                'nome': place['name'],
                'endereco': place['formatted_address'],
                'preco': place.get('price_level', 'vazio'),
                'nota': place['rating'],
                'votos': votos,
                'fone': fone
            }
        )
    token = places.get('next_page_token', False)
    if token:
        places = gmaps.places("Restaurantes em brasília", page_token=token)
    else:
        break
# gravar na planilha
wb = Workbook()
dest_filename = 'pesquisa.xlsx'
ws1 = wb.active
ws1.title = 'restaurantes'

ws1.append(list(dados_pesquisa[0].keys())) # adiciona o cabeçalho

for dados in dados_pesquisa:
    ws1.append(list(dados.values()))

wb.save(filename=dest_filename)



