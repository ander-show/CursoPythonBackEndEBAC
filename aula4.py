# Soma de 1 a N

# Receber um número aleatório

num_aleatorio = int(input("Digite um número aleatório: "))

# Criar lógica da soma

soma = 0

for i in range(1, num_aleatorio + 1):
    soma += i

# Exibir a soma de todos os números de 1 até N

print(soma)