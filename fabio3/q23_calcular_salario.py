# calculo_salario

def main():
    n = int(input("Quantidade de funcionários: "))
    calcular(n)

def calcular(n):
    i = 0

    while i < n:
        codigo = input("Código: ")
        horas = float(input("Horas: "))
        dependentes = int(input("Dependentes: "))

        bruto = horas * 12 + dependentes * 40
        inss = bruto * 0.085
        ir = bruto * 0.05
        liquido = bruto - inss - ir

        print("Funcionário:", codigo)
        print("INSS:", inss)
        print("IR:", ir)
        print("Líquido:", liquido)
        print()

        i += 1

main()