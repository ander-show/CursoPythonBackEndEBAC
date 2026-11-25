# Dado  um array de números inteiros, retorne quantos deles contem um numero par de digitos.
# Nums = [12, 345, 2, 6, 7896] -> valores inteiros
# Novo array = [12, 345, 2, 6, 7896] -> valores estarao como string

# 1 Criar um novo array com os valores convertidos para string

novo_array = ["12", "345", "2", "6", "7896"]

# 2 Fazer um looping dentro do novo_array para fazer a verificacao de numeros com digitos pares
# 3 fazer a contagem e mostrar o resultado

contador = 0

for i in novo_array:
    if len(i) % 2 == 0:
        contador += 1

        print(contador)
