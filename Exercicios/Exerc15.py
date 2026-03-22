print("=== Programa de Média de Notas ===")
notas = []
    
while True:
    try:
        nota = float(input("Digite a nota (ou -1 para sair): "))
            
        if nota == -1:
            break
        if nota < 0 or nota > 10:
            print("Erro: digite uma nota entre 0 e 10, ou -1 para sair.")
            continue

        notas.append(nota)

    except ValueError:
        print("Erro: digite apenas números válidos.")
    
if notas:
    media = sum(notas) / len(notas)
    print(f"\nMédia das notas: {media:.2f}")
else:
    print("\nNenhuma nota válida foi informada.")