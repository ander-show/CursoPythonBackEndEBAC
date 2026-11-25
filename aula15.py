# Uma classe é um molde.
# Vou usar esse molde para construir coisas que queremos que tem um mesmo padrão


class MoldePokemon:
    # Método construtor
    # Self armazena e manipula informações 
    def __init__(self, nome, hp, tipo, ataque, altura, peso):
        self.nome = nome
        self.hp = hp
        self.tipo = tipo
        self.ataque = ataque
        self.altura = altura
        self.peso = peso

    def mostrar_nome_pokemon(self):
        print(f"O nome do meu pokemon é: {self.nome}")

    def mostras_altura_pokemon(self):
        pass

    def mostrar_peso_pokemon(self):
        pass

pikachu = MoldePokemon("Pikachu", 400, "eletrico", 100, 50, 15)
charizard = MoldePokemon("charizard", 500, "fogo", 200, 200, 40)

pikachu.mostrar_nome_pokemon()
charizard.mostrar_peso_pokemon()