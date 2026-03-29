import collections

def situacao(media):
    if media >= 7:
        return "Aprovado"
    if media >= 5:
        return "Exame"
    return "Reprovado"

def main():
    Aluno = collections.namedtuple('Aluno', ['nome', 'nota1', 'nota2'])

    aluno = []
    for i in range(6):
        while True:
            try:
                nome = input(f"Digite o nome do aluno {i+1}: ")
                nota1 = float(input(f"Digite a primeira nota do aluno {i+1}: "))
                nota2 = float(input(f"Digite a segunda nota do aluno {i+1}: "))
                aluno.append(Aluno(nome, nota1, nota2))
                break
            except ValueError:
                print("Valor inválido. Por favor, digite um número para as notas.")

    linhas = []
    for a in aluno:
        media = sum([a.nota1, a.nota2]) / 2
        sit = situacao(media)
        nota1_str = (f"{n:.1f}" for n in [a.nota1])
        nota2_str = (f"{n:.1f}" for n in [a.nota2])
        linhas.append((a.nome, nota1_str, nota2_str, f"{media:.2f}", sit))

    print(f"{'Nome':<15}{'Nota1':<12}{'Nota2':<12}{'Média':>8}{' Situação':>12}")
    print("-" * 60)
    for nome, nota1_str, nota2_str, media_str, sit in linhas:
        print(f"{nome:<15}{next(nota1_str):<12}{next(nota2_str):<12}{media_str:>8}{sit:>12}")

    mediaClasse = sum(float(linhas[i][3]) for i in range(len(linhas))) / len(linhas)
    quantAprovados = sum(linhas[i][4] == "Aprovado" for i in range(len(linhas)))
    quantExame = sum(linhas[i][4] == "Exame" for i in range(len(linhas)))
    quantReprovados = sum(linhas[i][4] == "Reprovado" for i in range(len(linhas)))

    print("\nResumo da Turma:")
    print(f"Média da turma: {mediaClasse:.2f}")
    print(f"Quantidade de alunos aprovados: {quantAprovados}")
    print(f"Quantidade de alunos em exame: {quantExame}")
    print(f"Quantidade de alunos reprovados: {quantReprovados}")

if __name__ == "__main__":
    main()