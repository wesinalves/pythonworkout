# o que é para que serve
def fahrenheit(c):
  f = (9 / 5) * c + 32
  return f

for i in range(20):
  for j in range(1,6):
    print(f'C: {i*5 + j} \t F: {fahrenheit(i*5 + j):.2f}', end='\t')
  print()


# refatoração de código, módulo math
def prime(n):  
  for i in range(2,int(n/2)+1):
    if (n % i) == 0:
      return False
  
  return True

from math import sqrt

def prime_refined(n):  
  for i in range(2,int(sqrt(n))+1):
    if (n % i) == 0:
      return False
  
  return True

for p in range(2,100):
  print(f'{p} é um número primo? ', prime(p), prime_refined(p))


# argumentos padrão, argumentos palavra-chave
from random import randint

first = randint(0,10)
second = randint(0,10)

def question(a, b):
  text = f'Quanto é {a} x {b}: '
  return text

ask = question(first, second)

while(True):
  answer = input(ask)
  if int(answer) == 1000:
    break
  elif int(answer) == first * second:
    print('Muito bom!')
    first = randint(0,10)
    second = randint(0,10)
    ask = question(first, second)
  elif int(answer) != first * second:
    print("Não, tente novamente por favor")

# recursão e anotações
def solve_tower(disks, start, end, temp):
  if disks == 1:
    print(f'{start} -> {end}')
    return
  
  solve_tower(disks - 1, start, temp, end)
  print(f'{start} -> {end}')
  solve_tower(disks - 1, temp, end, start)
  

start = 1
end = 3
temp = 2
disks = 3

solve_tower(disks, start, end, temp)
