class Pizza(): #atributos: tipo y extra
    def __init__(self):
        self.tipo = ['pimentón, tofu, mozzarella y tomate','pepperoni, jamón, salmón, mozzarella y tomate'] #lista con los dos conjuntos de ingredientes según el tipo de pizza
        self.extra = ['Pimentón','Tofu', 'Pepperoni', 'Jamón', 'Salmón', 'mozzarella', 'tomate', 'ninguno'] #lista de ingredientes extra
    def __str__(self):
        print('''***BIENVENIDO A LA PIZZERIA BELLA NAPOLI***
            ¿Qué tipo de pizza desea?: 
            Opción 1: Vegetariana 
            Opción 2: No vegetariana''')
        tipo = int(input('Por favor, introduzca el número de opción deseada: '))
        i = int(input('Escoge uno entre los siguientes extras: pimiento(1), tofu(2), pepperoni(3), jamón(4), salmón(5), mozzarella(6), tomate(7), ninguno(8): '))
        if tipo == 1:
            return'Usted escogió una Pizza Vegetariana con {}y con el ingrediente extra: {} ¡Buen Provecho!'.format(self.tipo[0],self.extra[i-1])
        if tipo == 2:
            return 'Usted escogió una Pizza no Vegetariana con {} y con el ingrediente extra: {} ¡Buen Provecho!'.format(self.tipo[1],self.extra[i-1])
miPizza = Pizza()
print(str(miPizza))



        
   
    
    

    
    
    
    
        