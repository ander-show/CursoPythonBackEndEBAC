def meu_decorator(func):
    def wrapper():
        print("Antes da execução da minha despedida!")
        func()
        print("Depois da execução da minha despedida!")

    return wrapper


@meu_decorator
def despedida():
    print("Tchau")

@meu_decorator
def cheguei():
    print("Oiii")

cheguei()
despedida()