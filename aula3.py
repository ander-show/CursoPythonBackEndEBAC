# Receber um número e dizer a sua tabuada!

# Recebe um número do usuário

num_tabuada = float(input("Digite um número para ver sua tabuada: "))

# Criar lógica para calcular a tabuada

for i in range(1, 11):
    print(num_tabuada * i)