ingredientes = {'1': 'pimentón', '2': 'tofu', '3': 'pepperoni', '4': 'jamón', '5': 'salmón'}

def extra(ingrediente_extra):
    if ingrediente_extra == 1:
        i = (input('Escoge uno entre los siguientes extras: pimiento(1), tofu(2), pepperoni(3), jamón(4), salmón(5): '))
        print('Usted escogió el ingrediente extra: ' + (ingredientes[i]))
        print('¡Buen Provecho!')
    else:
        print('¡Buen Provecho!')

def tipo_de_pizza(pizza):
    if pizza == 1:
        eleccion_vegetariana = str(input('Escoja un ingrediente: Pimiento(1), Tofu(2): '))
        print(('Usted escogió una Pizza Vegetariana con Mozzarella, Tomate, y ') + ingredientes[eleccion_vegetariana])
        ingrediente_extra = int(input('¿Desea un ingrediente extra?: si(1) no(2)'))
        extra(ingrediente_extra)
    if pizza == 2:
        eleccion_no_vegetariana = int(input('Escoja un ingrediente: Pepperoni(3), Jamón(4), Salmón(5): '))                  
        print(('Usted escogió una Pizza Vegetariana con Mozzarella, Tomate, y ') + ingredientes[eleccion_no_vegetariana])
        ingrediente_extra = int(input('¿Desea un ingrediente extra?: si(1) no(2)'))
        extra(ingrediente_extra)

if __name__ == "__main__":
    print('''***BIENVENIDO A LA PIZZERIA BELLA NAPOLI***
            ¿Qué tipo de pizza desea?: 
            Opción 1: Vegetariana 
            Opción 2: No vegetariana''')
    pizza = int(input('Por favor, introduzca el número de opción deseada: '))
    tipo_de_pizza(pizza)