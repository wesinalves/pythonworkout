import random
def busca_binaria(key, vet):
    L = 0
    R = len(vet) - 1
    found = False
    while L <= R and not found:
        m = random.randint(L,R)
        if vet[m] == key:
            found = True
        else:
            if a[m] < key:
                L = m + 1
            else:
                R = m - 1 
    
    if not found:
        m = -1
    
    return m

if __name__ == "__main__":
    a = [8, 12, 19, 43, 45, 56, 67, 95]
    i = 0
    x = 45
    print(busca_binaria(x, a))

