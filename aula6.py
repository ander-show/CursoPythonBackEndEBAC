# Receba uma lista de palavras e coloque em ordem alfabética. Em seguida, imprima a lista ordenada.

# Criar array vazio para armazenar as palavras

lista_palavras = []

# Lógica para receber a lista de palavras do usuário

for i in range(1, 6):
    palavra = input("Digite uma palavra: ")
    lista_palavras.append(palavra)

lista_palavras.sort() 

# Mostrar lista em ordem alfabética

print(lista_palavras)