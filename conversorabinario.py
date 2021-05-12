#este programa es para calcular los números binarios utilizando la técnica de dividir entre 2 que explican en el curso de Pensamiento Lógico.
def calculo():
    decimal = int(input('Introduce un número: '))
    elegido = decimal
    binario = ''
    while (decimal > 0):
        resto = str(decimal % 2)
        binario = resto + binario
        decimal = decimal // 2
    print(str('El número decimal {} es en binario: {}'.format(elegido,binario))) 
           
if __name__ == "__main__":
    calculo()
    
