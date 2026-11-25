# Dado um array contendo n números distintos no intervalo [0,n]
# Retorne o único número no intervalo que está faltando no array.

meu_array = [0,2,3,4,5,6,7,8,9]

tamanho_meu_array = len(meu_array)
soma_valores_meu_array = sum(meu_array)

soma_total = (tamanho_meu_array * (tamanho_meu_array + 1)) // 2

print(soma_total - soma_valores_meu_array)