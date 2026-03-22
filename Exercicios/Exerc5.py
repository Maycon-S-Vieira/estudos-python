def gerar_html(nome, endereco, telefone, email, escolaridade, experiencia):
    """Gera o currículo em formato HTML."""
    html = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Currículo de {nome}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                line-height: 1.6;
            }}
            h1 {{
                color: #2c3e50;
            }}
            h2 {{
                color: #34495e;
                border-bottom: 1px solid #ccc;
            }}
            p {{
                margin: 5px 0;
            }}
        </style>
    </head>
    <body>
        <h1>{nome}</h1>
        <p><strong>Endereço:</strong> {endereco}</p>
        <p><strong>Telefone:</strong> {telefone}</p>
        <p><strong>E-mail:</strong> {email}</p>

        <h2>Escolaridade</h2>
        <p>{escolaridade}</p>

        <h2>Experiência Profissional</h2>
        <p>{experiencia}</p>
    </body>
    </html>
    """
    return html


def salvar_curriculo(nome_arquivo, conteudo_html):
    """Salva o currículo em um arquivo HTML."""
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo_html)
    print(f"Currículo salvo em {nome_arquivo}")


def main():
    nome = input("Digite seu nome completo: ")
    endereco = input("Digite seu endereço: ")
    telefone = input("Digite seu telefone: ")
    email = input("Digite seu e-mail: ")
    escolaridade = input("Digite sua escolaridade: ")
    experiencia = input("Digite sua experiência profissional: ")

    conteudo_html = gerar_html(nome, endereco, telefone, email, escolaridade, experiencia)
    salvar_curriculo("curriculo.html", conteudo_html)


if __name__ == "__main__":
    main()
