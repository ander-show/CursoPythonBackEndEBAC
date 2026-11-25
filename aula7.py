# Receba um número e determine se ele é palíndromo

# Receber um número do usuário

meu_numero = int(input("Digite um número: "))

minha_string = str(meu_numero)

# Determinar se é um palíndromo e dar o retorno

if minha_string == minha_string[::-1]:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")



