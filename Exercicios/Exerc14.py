def verificar_senha(senha):
    """Verifica se a senha atende aos critérios de segurança."""
    erros = []

    if len(senha) < 8:
        erros.append("A senha deve ter pelo menos 8 caracteres.")

    if not any(c.isupper() for c in senha):
        erros.append("A senha deve conter pelo menos uma letra maiúscula.")

    if not any(c.islower() for c in senha):
        erros.append("A senha deve conter pelo menos uma letra minúscula.")

    if not any(c.isdigit() for c in senha):
        erros.append("A senha deve conter pelo menos um número.")

    if not any(c in "!@#$%^&*()-_=+[]{};:,.<>?/\\|" for c in senha):
        erros.append("A senha deve conter pelo menos um caractere especial.")

    return erros


def main():
    print("=== Verificador de Senha ===")
    senha = input("Digite sua senha: ")

    erros = verificar_senha(senha)

    if erros:
        print("\nSenha inválida. Problemas encontrados:")
        for erro in erros:
            print(f"- {erro}")
    else:
        print("\nSenha válida! Está dentro dos critérios de segurança.")


if __name__ == "__main__":
    main()