# Receber nota do aluno

nota = float(input("Digite a nota do aluno: "))

# Fazer a operação e mostrar o resultado para o aluno.

if nota >= 7.0:
    print("Aluno aprovado!")
elif nota >= 5.0 and nota < 7.0:
    print("Aluno em recuperação!")
else:
    print("Aluno reprovado!")