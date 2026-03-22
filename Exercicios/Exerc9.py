def centuryFromYear(year):
    return (year + 99) // 100

year = int(input("Digite um ano: "))
print(centuryFromYear(year))