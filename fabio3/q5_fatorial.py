# fatorial

def main():
    n = int(input("N: "))
    print("Fatorial:", fatorial(n))

def fatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat *= i
    return fat

main()