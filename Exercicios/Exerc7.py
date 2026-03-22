for i in range(4):
    re = float(input("Digite o valor da resistencia: "))
    if i == 0:
        remaior = re
        remenor = re
    elif re > remaior:
        remaior = re
    elif re < remenor:
        remenor = re

print(f"A resistência maior é: {remaior}")
print(f"A resistência menor é: {remenor}")