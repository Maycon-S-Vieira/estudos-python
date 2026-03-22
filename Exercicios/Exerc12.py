import random
import sys


def play():
    number = random.randint(1, 100)
    attempts = 0
    print("Jogo da Adivinhação — adivinhe um número entre 1 e 100.")
    while True:
        try:
            guess = input("Seu palpite: ").strip()
            if not guess:
                print("Digite um número.")
                continue
            guess_int = int(guess)
        except ValueError:
            print("Por favor, digite um número inteiro.")
            continue
        except (EOFError, KeyboardInterrupt):
            print("\nEntrada interrompida. Saindo.")
            sys.exit()

        attempts += 1
        if guess_int < number:
            print("Mais alto.")
        elif guess_int > number:
            print("Mais baixo.")
        else:
            print(f"Parabéns! Você acertou em {attempts} tentativas.")
            break


def main():
    while True:
        play()
        try:
            again = input("Jogar novamente? (S/N): ").strip().upper()
        except (EOFError, KeyboardInterrupt):
            print("\nSaindo.")
            break
        if again != 'S':
            print("Até mais!")
            break


if __name__ == '__main__':
    main()
