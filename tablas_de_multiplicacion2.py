def run():

    numero = int(input("Introduce un número para ver su tabla de multiplicar: "))
    print("Esta es la tabla del " + str(numero))
    for i in range (1, 11):
        print(i * numero)

if __name__ == "__main__":
    run()




    

