p = input("Digite seu peso: ")
h = input("Digite sua altura: ")

imc = float(p) / (float(h) ** 2)
print(f"Seu IMC é: {imc:.2f}")