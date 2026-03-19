# serie_alternada

def main():
    n = int(input("N: "))
    print(f"S = {soma(n):.2f}")

def soma(n):
    num = 1
    den = n
    total = 0
    sinal = 1

    while den >= 1:
        total += sinal * (num / den)
        num += 1
        den -= 2
        sinal *= -1

    return total

main()