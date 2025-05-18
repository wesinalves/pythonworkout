def busca_linear_sentinela(key, vet):
    i = 0
    N = len(vet) - 1
    while vet[i] != key:
        i += 1
    
    if i == N:
        i = -1
    
    return i

if __name__ == "__main__":
    a = [45, 56, 12, 43, 95, 19, 8, 67]
    i = 0
    x = 81
    a.append(x)
    print(busca_linear_sentinela(x, a))

