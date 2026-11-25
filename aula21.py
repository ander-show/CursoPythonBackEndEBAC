# lambda é uma função que não precisa ser inicializada 

meu_array = [1, 2, 3, 4, 5]

duplicados = map(lambda numero : numero * 2, meu_array)

print(list(duplicados))