##############################################################################33
numbers = ()
# ler quinze números
for _ in range(15):
  print(numbers)
  x = int(input('Digite um número: '))
  # se não for duplicado, imprime o número  
  if not (x in numbers):
    print(f'{x} não está duplicado.')
  numbers = list(numbers)     
  numbers.append(x)
  numbers = tuple(numbers)

########################################################################
# ler informações do mês
from random import randint
sales = []

for d in range(30):
  for s in range(3):
    for p in range(4):
      sales.append([s, p, randint(0,20)])
# resumo do total de vendas por vendedor e produto
# # todos os totais devem ser armazenados em vendas
total_sales = [[0 for p in range(4)] for s in range(3)]

for s in range(3):
  for p in range(4):
    for sale in sales:
      if sale[0] == s and sale[1] == p:
        total_sales[s][p] = total_sales[s][p] + sale[2]

print(total_sales)
print('\t\tsalesman1\t salesman2 \t salesman3 \t total')
for p in range(4):
  print(f'product{p}', end='')
  print(f'\t {total_sales[0][p]}', end='\t')
  print(f'\t {total_sales[1][p]}', end='\t')
  print(f'\t {total_sales[2][p]}', end='\t')
  total_products = sum([row[p] for row in total_sales])
  print(f'\t {total_products}')
print(f'total \t\t{sum(total_sales[0])}\t\t{sum(total_sales[1])}\
\t\t{sum(total_sales[2])}')

# # formato tabular, colunas -> vendedores, linhas -> produtos
#              vendedor 1, vendedor 2, vendedor 3
# produto1                                          total p1
# produto2                                          total p2
# produto3                                          total p3
# produto4                                          total p4
#              total v1, total v2, total v3

########################################################################
# criar função
def bubble_sort(vector):
    '''Sort a vector in ascending order.'''
    length = len(vector)
    # percorrer a lista
    for i in range(length):
        for j in range(length - i - 1):
            #comparar cada par adjacente
            if vector[j] > vector[j+1]:
                # troca elementos
                vector[j], vector[j+1] = vector[j+1], vector[j]

# gerando um vetor aleatório com 10 números
elements = [randint(0, 100) for _ in range(10)]
print(elements)
# aplicar o método bubble sort no vetor
bubble_sort(elements)
print(elements)

##############################################################3
# Dictionary representing the morse code chart
morse = { 'A':'.-', 'B':'-...',
          'C':'-.-.', 'D':'-..', 'E':'.',
          'F':'..-.', 'G':'--.', 'H':'....',
          'I':'..', 'J':'.---', 'K':'-.-',
          'L':'.-..', 'M':'--', 'N':'-.',
          'O':'---', 'P':'.--.', 'Q':'--.-',
          'R':'.-.', 'S':'...', 'T':'-',
          'U':'..-', 'V':'...-', 'W':'.--',
          'X':'-..-', 'Y':'-.--', 'Z':'--..',
          '1':'.----', '2':'..---', '3':'...--',
          '4':'....-', '5':'.....', '6':'-....',
          '7':'--...', '8':'---..', '9':'----.',
          '0':'-----'}

# função para traduzir a mensagem
def translate(message):
  code = ''
  for letter in message:
    if letter in morse:
      code += morse[letter] + ' '
    else:
      code += ''
  return code

# testar a função tradução
my_message = input('Digite sua mensagem: ')
print(translate(my_message.upper()))