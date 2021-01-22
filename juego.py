import random


def run():
    numero_aleatorio = random.randint(1, 100)
    contador = 0
    numero_elegido = int(input("Elige un número del 1 al 100:  "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Busca un número más grande")
        else:
            print("Busca un número más pequeño")
        numero_elegido = int(input("Elige otro número: "))
        contador = contador + 1
    print("¡Ganaste! Lo lograste en " + str(contador) + " intentos")
    


if __name__ == "__main__":
    run()