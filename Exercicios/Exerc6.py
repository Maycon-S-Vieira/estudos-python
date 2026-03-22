nome = input("Digite o nome do produto:")
valor = float(input("Digite o valor do produto:"))
while valor < 0:
    print("Valor inválido. Digite um valor maior que 0.")
    valor = float(input("Digite o valor do produto:"))

if valor >= 50 and valor < 200:
    desconto = valor * 0.95
elif valor >= 200 and valor < 500:
    desconto = valor * 0.94
elif valor >= 500 and valor < 1000:
    desconto = valor * 0.93
elif valor >= 1000:
    desconto = valor * 0.92

print(f"O valor do produto {nome} com desconto é:",
      f"R${desconto:.2f} e o seu valor original é: R${valor:.2f}")