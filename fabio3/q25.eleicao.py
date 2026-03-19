# eleicao

def main():
    n = int(input("Quantidade de eleitores: "))
    eleicao(n)

def eleicao(n):
    c1 = c2 = c3 = nulo = branco = 0

    i = 0
    while i < n:
        voto = int(input("Voto: "))

        if voto == 1:
            c1 += 1
        elif voto == 2:
            c2 += 1
        elif voto == 3:
            c3 += 1
        elif voto == 9:
            nulo += 1
        elif voto == 0:
            branco += 1

        i += 1

    print("C1:", c1)
    print("C2:", c2)
    print("C3:", c3)
    print("Nulos:", nulo)
    print("Brancos:", branco)

    if c1 > c2 and c1 > c3:
        print("Vencedor: Candidato 1")
    elif c2 > c1 and c2 > c3:
        print("Vencedor: Candidato 2")
    elif c3 > c1 and c3 > c2:
        print("Vencedor: Candidato 3")
    else:
        print("Empate")

main()