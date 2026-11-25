# SuperClasse
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print("O animal emitiu um som genérico.")

# SubClasse
class Cachorro(Animal):
    def emitir_som(self):
        print("O cachorro latiu!")

# SubClasse
class Gato(Animal):
    def emitir_som(self):
        print("O gato miou!")

# Criando objetos
cachorro = Cachorro("Max", 5)
gato = Gato("Garfield", 3)

# Exibindo métodos
cachorro.emitir_som()

gato.emitir_som()
