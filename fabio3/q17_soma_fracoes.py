# soma_fracoes

def main():
    n = int(input("N: "))
    print(f"S = {soma(n):.2f}")

def soma(n):
    total = 0
    for i in range(1, n+1):
        total += 1 / i
    return total

main()