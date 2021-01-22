# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
# * Ingredientes vegetarianos: Pimiento y tofu.
# * Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva. Además también debes preguntale al cliente si quiere un adicional en su elección
class Pizza():
    def __init__(self):
        self.vegetariana = 'pimentón, tofu, mozzarella y tomate'
        self.no_vegetariana = 'pepperoni, jamón, salmón, mozzarella y tomate'
        
    def __str__(self):
        print('''***BIENVENIDO A LA PIZZERIA BELLA NAPOLI***
            ¿Qué tipo de pizza desea?: 
            Opción 1: Vegetariana 
            Opción 2: No vegetariana''')
        tipo = int(input('Por favor, introduzca el número de opción deseada: '))
        if tipo == 1:
            return'Usted escogió una Pizza Vegetariana con {}'.format(self.vegetariana)
        if tipo == 2:
            return 'Usted escogió una Pizza no Vegetariana con {}'.format(self.no_vegetariana)
class Extra():
    def __init__(self):
        self.extra = ['Pimentón','Tofu', 'Pepperoni', 'Jamón', 'Salmón', 'mozzarella', 'tomate', 'ninguno']

    def __str__(self):
        i = int(input('Escoge uno entre los siguientes extras: pimiento(1), tofu(2), pepperoni(3), jamón(4), salmón(5), mozzarella(6), tomate(7), ninguno(8): '))
        return 'Usted escogió el ingrediente extra: {} ¡Buen Provecho!'.format(self.extra[i-1])

miPizza = Pizza()
print(str(miPizza))
miExtra = Extra()
print(str(miExtra))



        
   
    
    

    
    
    
    
        