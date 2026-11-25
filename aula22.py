try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(resultado)
    
except ValueError:
    print("Erro: entrada inválida. Por favor digite um número!")
except ZeroDivisionError:
    print("Não existe divisão por zero!")