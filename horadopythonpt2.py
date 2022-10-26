total_liters = 0
total_kilometers = 0

while(True):
  liters = int(input("Forneça a quantidade de litros: "))
  kilometers = int(input("Forneça a quantidade de km: "))
  total_liters += liters
  total_kilometers += kilometers
  keep = input("Deseja continuar? (s/n): ")
  if keep == 'n':
    break

print(f"A média de consumo do carro é igual a {total_kilometers/total_liters}")


#################################3

number = int(input('Forneça um número com 5 digitos: '))
modulos = [0 for _ in range(5)]
for n in range(4,-1,-1):  
  modulos[n] = number % 10
  print(number // 10, number % 10)  
  number = number // 10

print(modulos)
if modulos[0] == modulos[4] and modulos[1] == modulos[3]:
  print(f"O número {''.join(str(a) for a in modulos)} é um palindrome!")
else:
  print(f"O número {''.join(str(a) for a in modulos)} não é um palindrome!")


####################################################

byte = input('Forneça o número binario: ')
length = len(byte)
byte = int(byte)
value = 0

for n in range(length):
  bit = byte % 10
  print(byte, bit)
  byte = byte // 10
  value += bit * 2 ** n 

print(f'O valor decimal equivalente é {value}')

###########################################################

number = int(input('Forneça o número: '))
if number < 0:
  raise ValueError('O número precisa ser maior que 0')

fatorial = 1
for n in range(number):
  fatorial *= number - n

print(fatorial)

terms = int(input('Forneça o número de termos: '))
e = 0
for i in range(terms):
  fatorial = 1
  for n in range(i):
    fatorial *= i - n
  e += 1 / fatorial
print(e)
# 2.718281828459045235360287

terms = int(input('Forneça o número de termos: '))
x = int(input('Forneça o valor de x: '))
e_x = 0
for i in range(terms):
  fatorial = 1
  for n in range(i):
    fatorial *= i - n
  e_x += (x ** i) / fatorial

print(e_x)

####################################################################

for i in range(10):
  print('*'*(i+1))

for i in range(10,0,-1):
  print('*'*i)

for i in range(10,0,-1):
  print(' '*(10 - i), end='')
  print('*'*i)

for i in range(10):
  print(' '*(10 - i), end='')
  print('*'*(i+1))

########################################################################

for a in range(1,21):
  for b in range(1,21):
    for h in range(1,21):      
      if h ** 2 == a ** 2 + b ** 2:
        print('h^2 = a^2 + b^2: ', h, a, b)