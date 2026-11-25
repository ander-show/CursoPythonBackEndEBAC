# Dada um array de números inteiros, retorne a soma do menor número e do maior número do array.

meu_array = [3, 5, 1, 8, 2]

# 1. Vamos ordenar o array para encontrar o menor e o maior número

meu_array.sort()

# 2. Somar o primeiro e o último número do array ordenado

primeiro_valor = meu_array[0]
ultimo_valor = meu_array[-1]

print(primeiro_valor + ultimo_valor)