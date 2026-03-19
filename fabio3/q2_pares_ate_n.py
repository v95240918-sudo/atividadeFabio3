# pares_ate_n

def main():
    n = int(input("N: "))
    pares(n)

def pares(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i)

main()