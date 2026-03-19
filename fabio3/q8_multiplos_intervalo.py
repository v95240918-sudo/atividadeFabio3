# multiplos_intervalo

def main():
    n = int(input("N: "))
    inf = int(input("Inferior: "))
    sup = int(input("Superior: "))
    multiplos(n, inf, sup)

def multiplos(n, inf, sup):
    for i in range(inf, sup+1):
        if i % n == 0:
            print(i)

main()