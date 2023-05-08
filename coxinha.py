import timeit

def barraca_return(pedidos):
  # processa todos os pedidos primeiro
  # então retorna todos os pedidos
  output = []
  for pedido in pedidos:
    output.append(f'{pedido} coxinhas')
  return output

def barraca_yield(pedidos):
  # processa 1 pedido, então o retorna
  # repete até todos os pedidos terminarem
  for pedido in pedidos:
    yield f'{pedido} coxinhas'

def main():
    start_return = timeit.default_timer()
    for pedido in barraca_return([100 for _ in range(100000)]):
        #print(f'saindo {pedido} coxinhas na barraca return')
        pass
    
    stop_return = timeit.default_timer()
    print('return time', stop_return - start_return)
    
    start_yeld = timeit.default_timer()
    for pedido in barraca_yield([100 for _ in range(100000)]):
        #print(f'saindo {pedido} coxinhas na barraca yield')
        pass
    
    stop_yield = timeit.default_timer()
    print('yield time', stop_yield - start_yeld)

main()