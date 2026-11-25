# Lista operações      
operacoes = ["soma", "subtracao", "multiplicacao", "divisao"]

# Lógica calculadora
soma = lambda a,b: a + b
subtracao = lambda a,b: a - b
multiplicacao = lambda a,b: a * b
divisao = lambda a,b: a / b

while True:
# Pedindo num1
    while True:
        try:
            numero1 = int(input("Digite o primeiro número: "))
            break
        except ValueError:
            print("Erro! Digite um número válido!")
        
# pedindo num2
    while True:
        try:
           numero2 = int(input("Digite o segundo número: "))
           break
        except ValueError:
           print("Erro! Digite um número válido!")
        
# Seleção da operação
    menu = [f"{i + 1} - {operacao}" for i, operacao in enumerate(operacoes)]

# Mostrando menu
    print("\n---Calculadora---")

    for item in menu:
       print(item)
# Validação de opção
    while True:
       opcao = input("Escolha uma operação: ")

       if opcao in ["1", "2", "3", "4"]:
          break
       else:
          print("Opção inválida!")

# Realização de operação
    if opcao == "1":
        resultado = soma(numero1, numero2)

    elif opcao == "2":
        resultado = subtracao(numero1, numero2)

    elif opcao == "3":
        resultado = multiplicacao(numero1, numero2)

    elif opcao == "4":
        
# Divisão por zero
        while numero2 == 0:
           print("Erro! Divisão por zero não é permitida.")

           try:
              numero2 = int(input("Digite outro divisor: "))

           except ValueError:
              print("Erro! Digite um número válido.")
              numero2 = 0

        resultado = divisao(numero1, numero2)

# Mostrar resultado
    print(f"Resultado: {resultado}")

# Continuar?
    continuar = input("Deseja realizar outra operação: (s/n): ")

    if continuar.lower() != "s":
       print("Calculadora encerrada!")
       break
