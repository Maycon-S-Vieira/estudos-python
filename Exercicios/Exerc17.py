def main():
    vetor = []

    for i in range(6):
        while True:
            try:
                vetor.append(int(input(f"Digite um numero inteiro: ")))
                break
            except ValueError:
                print("Valor inválido. Por favor, digite um número.")

    pares =  sum(n % 2 == 0 for n in vetor)
    impares = sum(n % 2 != 0 for n in vetor)
    soma = sum(vetor)
    maior = max(vetor)
    menor = min(vetor)
    positivos = sum(n > 0 for n in vetor)

    print("Números pares:", pares)
    print("Números ímpares:", impares)
    print("Soma:", soma)
    print("Maior:", maior)
    print("Menor:", menor)
    print("Positivos:", positivos)

if __name__ == "__main__":
    main()

