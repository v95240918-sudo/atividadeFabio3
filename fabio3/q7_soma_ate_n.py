# soma_ate_n

def main():
    n = int(input("N: "))
    print("Soma:", soma(n))

def soma(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

main()