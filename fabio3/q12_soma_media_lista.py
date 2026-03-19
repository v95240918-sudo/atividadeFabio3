# soma_media_lista

def main():
    n = int(input("Quantidade: "))
    soma, media = calcular(n)
    print("Soma:", soma)
    print("Média:", media)

def calcular(n):
    soma = 0
    for i in range(n):
        num = float(input("Número: "))
        soma += num
    return soma, soma/n

main()