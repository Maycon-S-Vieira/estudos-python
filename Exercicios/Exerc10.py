def calcular_imc(peso, altura):
    """Calcula o IMC dado peso e altura."""
    return peso / (altura ** 2)


def main():
    while True:
        try:
            peso = float(input("Digite o peso (kg): "))
            altura = float(input("Digite a altura (m): "))

            if peso <= 0 or altura <= 0:
                raise ValueError("Peso e altura devem ser maiores que zero.")

            imc = calcular_imc(peso, altura)
            print(f"IMC: {imc:.2f}")

        except ValueError as e:
            print(f"Entrada inválida: {e}")
            continue

        continuar = input("Deseja continuar? (s/n): ").strip().lower()
        if continuar != "s":
            print("Encerrando o programa.")
            break


if __name__ == "__main__":
    main()
