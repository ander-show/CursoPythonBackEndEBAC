produtos = {}

# 1. Adicionar produtos

def adicionar_produto():
    nome = (input("Digite o nome do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    preco = float(input("Digite o preço do produto: "))

    produtos[nome] = {
        "quantidade": quantidade,
        "preco": preco
    }

    print("Produto adicionado com sucesso!")

# 2. Listar produtos

def listar_produtos():
    for nome in sorted(produtos, key=lambda x: x.lower()):
        quantidade = produtos[nome]["quantidade"]
        preco = produtos[nome]["preco"]

        print(f"{nome}: {quantidade} disponiveis - R$ {preco:.2f}")

# 3. Remover produtos

def remover_produtos():

    nome = input("Digite o nomer do produto que deseja remover: ")

    if nome in produtos:
       del produtos[nome]
       print("Produto removido com sucesso!")
    else:
       print("Erro: Produto não encontrado")

# 4. Atualizar produtos

def atualizar_produtos():

    nome = input("Digite o nome do produto: ")

    if nome in produtos:

        nova_quantidade = int(input("Digite a nova quantidade: "))

        produtos[nome]["quantidade"] = nova_quantidade

        print("Quantidade atualizada com sucesso!")

    else:
        print("Erro: Produto não encontrado")
    

# MENU
def menu():
    print("=== MENU ===")
    print("1. Adicionar produtos")
    print("2. Listar produtos")
    print("3. Remover produtos")
    print("4. Atualizar produtos")
    print("5. Sair do programa")

# Pergunta ao usuário qual opção ele deseja escolher

while True:

   menu()

   opcao = input("Escolha uma opção: ")

   if opcao == "1":
       adicionar_produto()
   elif opcao == "2":
       listar_produtos()
   elif opcao == "3":
       remover_produtos()
   elif opcao == "4":
       atualizar_produtos()
   elif opcao == "5":
       print("Você escolheu a opção 5: Sair do programa")
       break

   else:
       print("Opção inválida. Por favor, escolha uma opção válida.")