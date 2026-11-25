#Escrevendo um programa que recebe 3 números e diz qual o segundo maios.

# Recebendo numeros separadamente

numero1, numero2, numero3 = map(int, input().split())

# Lógica para ver quem é o segundo maior

meu_array = []

meu_array.append(numero1)
meu_array.append(numero2)
meu_array.append(numero3)

meu_array.sort()

print(meu_array)

# Mostrando o segundo maior número

print(meu_array[1])

