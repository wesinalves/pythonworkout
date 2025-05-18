def busca_linear(key, vet):
    i = 0
    N = len(vet)
    while i < N and vet[i] != key:
        i += 1
    
    if i == N:
        i = -1
    
    return i

if __name__ == "__main__":
    a = [45, 56, 12, 43, 95, 19, 8, 67]
    i = 0
    x = 19
    print(busca_linear(x, a))