# Você recebe um array de números inteiros meu_arrayzinho
# Os elementos de um array são os elementos que aparecem exatamente uma vez no array.
# Retorne a soma de todos os elementos únicos de meu_arrayzinho.

meu_arrayzinho = [1,2,3,3,2,4,5,5,7,6,6,33,44,55]

# 1. Criar um dicionário adicionar a chave e valor

meu_dicionario = {}

for i in meu_arrayzinho:
    if i not in meu_dicionario:
        meu_dicionario[i] = 1
    else:
        meu_dicionario[i] += 1

# 2. Encontrar os valores que aparecem exatamente uma vez
# 3. Somar valores das chaves que aparecem exatamente uma vez

soma_das_chaves_unicas = 0

for chave, valor in meu_dicionario.items():
    if valor == 1:
        soma_das_chaves_unicas += chave

        print(soma_das_chaves_unicas)

