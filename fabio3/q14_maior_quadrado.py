# maior_quadrado

def main():
    n = int(input("N: "))
    print("Maior quadrado:", calcular(n))

def calcular(n):
    i = 1
    while i*i <= n:
        i += 1
    return (i-1)**2

main()