def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b


def ler_inteiro(mensagem):
    """Força o usuário a digitar apenas inteiros."""
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Erro: digite apenas números inteiros.")


def menu():
    """Exibe o menu e força escolha válida."""
    while True:
        print("\nEscolha a operação:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")

        try:
            opcao = int(input("Digite sua opção (1 a 4): "))
            if opcao in [1, 2, 3, 4]:
                return opcao
            else:
                print("Erro: escolha apenas entre 1 e 4.")
        except ValueError:
            print("Erro: digite apenas números inteiros.")


def main():
    print("=== Calculadora Simples ===")
    num1 = ler_inteiro("Digite o primeiro número inteiro: ")
    num2 = ler_inteiro("Digite o segundo número inteiro: ")

    opcao = menu()

    if opcao == 1:
        resultado = soma(num1, num2)
        print(f"Resultado da soma: {resultado}")
    elif opcao == 2:
        resultado = subtracao(num1, num2)
        print(f"Resultado da subtração: {resultado}")
    elif opcao == 3:
        resultado = multiplicacao(num1, num2)
        print(f"Resultado da multiplicação: {resultado}")
    elif opcao == 4:
        try:
            resultado = divisao(num1, num2)
            print(f"Resultado da divisão: {resultado}")
        except ZeroDivisionError as e:
            print(f"Erro: {e}")


if __name__ == "__main__":
    main()
