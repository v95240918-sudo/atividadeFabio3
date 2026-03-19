# maior_lista

def main():
    n = int(input("Quantidade: "))
    print("Maior:", maior(n))

def maior(n):
    maior = float(input("Número: "))
    for i in range(n-1):
        num = float(input("Número: "))
        if num > maior:
            maior = num
    return maior

main()