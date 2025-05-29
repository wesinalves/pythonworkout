def busca_binaria(key, vet):
    L = 0
    R = len(vet) - 1
    while L < R:
        # cálculo da mediana
        m = (L + R) // 2 # divisão inteira
        if a[m] < key:
            L = m + 1
        else:
            R = m 
    
    if a[R] == key: # condição de igualdade
        return R
    
    return -1

if __name__ == "__main__":
    a = [8, 12, 19, 43, 45, 56, 67, 95]
    i = 0
    x = 67
    print(busca_binaria(x, a))

