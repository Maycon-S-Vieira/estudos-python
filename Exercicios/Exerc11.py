import array as arr

def parImpar(num):
    return "par" if num % 2 == 0 else "ímpar"
    
def maiorIdade(idade):
    return "maior de idade" if idade >= 18 else "menor de idade"
    
def conversor(valor):
    return valor * 5

def situacao(nota):
    return "aprovado" if nota >= 6 else "reprovado"
    
def maior(numMaior):
    return max(numMaior)

def negPos(numP):
    return "Negativo" if numP < 0 else "Positivo" if numP > 0 else "Zero"
    
def defSexo(sexo):
    return "Masculino" if sexo == 'M' else "Feminino"

def calcular_tabua(numT):
    for i in range(1, 11):
        print(f"{numT} x {i} = {numT * i}")

def numero_inteiro():
    while True:
        try:
            num = int(input("Digite um número inteiro: "))
            return num
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

# 1 ---
nome = input("Digite seu nome: ")
print(f"\nOlá, {nome}!\nBem-vindo!\n")

# 2 ---
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print(f"A soma de {n1} e {n2} é: {n1 + n2}\n")

# 3 ---
idade = int(input("Digite sua idade: "))
print(f"Você é {maiorIdade(idade)}.\n")

# 4 ---
num = numero_inteiro()

print(f"O número {num} é {parImpar(num)}.\n")

# 5 ---
valor = float(input("Digite um valor em reais: "))
print(f"O valor em dólares é: {conversor(valor)}\n")

# 6 ---
nota = float(input("Digite sua nota: "))
print(f"Você está {situacao(nota)}.\n")

# 7 ---
numMaior = arr.array('f')
for i in range(3):
    numM = float(input(f"Digite o {i+1}º número: "))
    numMaior.append(numM)

print(f"O maior número é: {maior(numMaior)}\n")

# 8 ---
numP = float(input("Digite um número: "))
print(f"O número é {negPos(numP)}.\n")

# 9 ---
salario = float(input("Digite o salário: "))

print(f"O salário com aumento é: {salario * 1.15}\n")

# 10 ---
while True:
    sexo = input("Digite o sexo (M/F): ").strip().upper()
    if sexo in ('M', 'F'):
        break
    print("Sexo inválido. Por favor, digite M ou F.")

print(f"O sexo é: {defSexo(sexo)}.\n")

# 11 ---
for i in range(1, 11):
    print(f"{i} x {num} = {i * num}\n")

# 12 ---
pares = [i for i in range(1, 21) if i % 2 == 0]
print(f"Numeros pares entre 1 e 20: {pares}\n")

# 13 ---
num = numero_inteiro()

print(f"Tabuada do {num}: ")
calcular_tabua(num)
print("\n")

# 14 ---
soma = 0

while True:
    numS = float(input("Digite um número (0 para sair): "))
    if numS == 0:
        break
    soma += numS

print(f"A soma dos números é: {soma}\n")

# 15 ---
pares2 = []

print("Digite números inteiros (0 para sair)")
while True:
    numerosP = numero_inteiro()
    if numerosP == 0:
        break
    if parImpar(numerosP) == "par":
        pares2.append(numerosP)

print(f"Numeros pares: {pares2}\n")