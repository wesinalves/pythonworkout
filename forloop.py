import random
price = 0
for _ in range(random.randint(5,15)):
    price = price + 1
    if price == 10:
        break
else:
    print('price never got 10...')