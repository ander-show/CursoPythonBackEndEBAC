# List comprehension / horizontal

quadrados_impares = [elemento**2 for elemento in range(1,11) if elemento %2 != 0]

# Mesmo código vertival

novo_array = []

for elemento in range(1,11):
    novo_array.append(elemento**2)

for elemento in novo_array:
    if elemento % 2 != 0:
        print(elemento)