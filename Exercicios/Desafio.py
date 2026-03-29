import collections
import random
import string

def usernameCreator(nome):
    username = nome[0].lower() + nome.lower().strip().split()[-1]
    return username

def senhaCreator():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(8))
    return senha


def main():
    contadorUsername = 0
    Aluno = collections.namedtuple('Aluno', ['nome', 'username', 'senha'])

    aluno = []
    for i in range(5):
        while True:
            try:
                nome = input(f"Digite o nome do aluno {i+1}: ")
                username = usernameCreator(nome)

                for i in range(len(aluno)):
                    if aluno[i].username == username:
                        username += str(contadorUsername + 1)
                        contadorUsername += 1

                senha = senhaCreator()
                aluno.append(Aluno(nome, username, senha))
                break
            except ValueError:
                print("Valor inválido. Por favor, digite um nome válido.")

    aluno.sort(key=lambda x: x.nome)

    print(f"{'Nome':<30}{'Username':<20}{'Senha':<20}")
    print("-" * 60)
    for a in aluno:
        print(f"{a.nome:<30}{a.username:<20}{a.senha:<20}")

if __name__ == "__main__":
    main()