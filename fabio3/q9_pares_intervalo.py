# pares_intervalo

def main():
    inf = int(input("Inferior: "))
    sup = int(input("Superior: "))
    pares(inf, sup)

def pares(inf, sup):
    for i in range(inf, sup+1):
        if i % 2 == 0:
            print(i)

main()