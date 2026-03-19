# sequencia_triangular

def main():
    n = int(input("N: "))
    sequencia(n)

def sequencia(n):
    soma = 0
    for i in range(1, n+1):
        soma += i
        print(soma)

main()