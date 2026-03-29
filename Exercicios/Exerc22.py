def main():
    vetor = []

    for i in range(15):
        while True:
            try:
                vetor.append(int(input(f"Digite um numero inteiro: ")))
                break
            except ValueError:
                print("Valor inválido. Por favor, digite um número.")

    maior = max(vetor)

    for i in range(len(vetor)):
        vetor[i] = vetor[i] / maior

    print("Novo vetor: ", vetor)

if __name__ == "__main__":
    main()