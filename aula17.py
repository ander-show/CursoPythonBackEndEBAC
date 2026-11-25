# Polimorfismo

class Animal:
   def falar(self):
      pass

class Cachorro(Animal):
   def falar(self):
      return "Au Au"

class Gato(Animal):
   def falar(self):
      return "Miau Miau"

animais = (Cachorro(), Gato())

for animal in animais:
   print(animal.falar() )