# Dada um array de números inteiros, cada elemento aparece duas vezes, exceto um. Encontre ele

meu_array = [1,1,2,2,3,3,4,5,5,6,6]

# 1. Criar um dicionário adicionar a chave e valor

meu_dicionario = {}

for i in meu_array:
    if i not in meu_dicionario:
        meu_dicionario[i] = 1
    else:
        meu_dicionario[i] += 1

# 2. Verificar qual valor aparece apenas uma vez

for chave, valor in meu_dicionario.items():
    if valor == 1:
        print(chave)
        