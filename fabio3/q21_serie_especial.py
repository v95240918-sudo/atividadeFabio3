# serie_especial

def main():
    print(f"S = {soma():.2f}")

def soma():
    total = 0
    num = 1
    for den in range(1, 51):
        total += num / den
        num += 2
    return total

main()