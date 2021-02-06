def calculo():
    decimal = int(input('Introduce un número: '))
    binario = ''
    while (decimal > 0):
        resto = str(decimal % 2)
        binario = resto + binario
        decimal = decimal // 2
    print(str(binario)) 
           
if __name__ == "__main__":
    calculo()
    