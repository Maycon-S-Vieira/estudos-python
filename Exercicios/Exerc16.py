import time

def contador_regressivo(inicio):
    for i in range(inicio, -1, -1):
        print(i)
        time.sleep(1)
    print("Fim da contagem!")

def main():
    while True:
        try:
            numero = int(input("Digite um número inteiro positivo para iniciar a contagem regressiva: "))
            if numero < 0:
                print("Erro: digite apenas números inteiros positivos.")
                continue
            contador_regressivo(numero)
            break
        except ValueError:
            print("Erro: digite apenas números inteiros.")

if __name__ == "__main__":
    main()
