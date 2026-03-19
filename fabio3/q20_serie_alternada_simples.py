# serie_alternada_simples

def main():
    n = int(input("N: "))
    print(f"S = {soma(n):.2f}")

def soma(n):
    total = 0
    sinal = 1
    for i in range(1, n+1):
        total += sinal * (1 / i)
        sinal *= -1
    return total

main()