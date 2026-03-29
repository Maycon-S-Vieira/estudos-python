import collections

def main():
    Produto = collections.namedtuple('Produto', ['nome', 'valor'])

    produto = []
    for i in range(5):
        while True:
            try:
                nome = input(f"Digite o nome do produto {i+1}: ")
                valor = float(input(f"Digite o valor do produto {i+1}: "))
                produto.append(Produto(nome, valor))
                break
            except ValueError:
                print("Valor inválido. Por favor, digite um número para as notas.")

    precoInf = sum(produto[i].valor < 50 for i in range(len(produto)))
    nomes = [produto[i].nome for i in range(len(produto)) 
             if produto[i].valor > 50 and produto[i].valor < 100 ]
    try:
        media = sum(produto[i].valor for i in range(len(produto)) 
                    if produto[i].valor > 100) / sum(produto[i].valor > 100 for i in range(len(produto)))
    except ZeroDivisionError:
        media = 0

    print(f"Quantidade de produtos com preço inferior a R$ 50,00: {precoInf}")
    print(f"Nome dos produtos com preço entre R$ 50,00 e R$ 100,00:  {', '.join(map(str, nomes))}")
    print(f"Média dos valores dos produtos com preço superior a R$ 100,00: {media:.2f}")

if __name__ == "__main__":
    main()