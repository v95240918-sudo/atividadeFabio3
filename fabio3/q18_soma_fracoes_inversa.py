# soma_fracoes_inversa

def main():
    n = int(input("N: "))
    print(f"S = {soma(n):.2f}")

def soma(n):
    total = 0
    for i in range(n, 0, -1):
        total += 1 / i
    return total

main()