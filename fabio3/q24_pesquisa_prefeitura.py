# pesquisa_prefeitura

def main():
    n = int(input("Quantidade de pessoas: "))
    pesquisa(n)

def pesquisa(n):
    i = 0
    soma_salario = 0
    soma_filhos = 0
    ate_1000 = 0

    while i < n:
        salario = float(input("Salário: "))
        filhos = int(input("Filhos: "))

        soma_salario += salario
        soma_filhos += filhos

        if salario <= 1000:
            ate_1000 += 1

        i += 1

    print("Média salário:", soma_salario / n)
    print("Média filhos:", soma_filhos / n)
    print("Percentual até 1000:", (ate_1000 / n) * 100, "%")

main()