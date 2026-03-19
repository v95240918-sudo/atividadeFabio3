# progressao_geometrica

def main():
    a0 = int(input("A0: "))
    limite = int(input("Limite: "))
    r = int(input("Razão: "))
    pg(a0, limite, r)

def pg(a0, limite, r):
    termo = a0
    while termo < limite:
        print(termo)
        termo *= r

main()