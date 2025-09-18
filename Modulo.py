'''
import mod_funciones
#Función principal
numero = int(input("Ingrese un número entero mayor que 1: "))
mod_funciones.primo(numero)
variable = int(input("Ingrese el número de términos de la serie de Fibonacci: "))
mod_funciones.fibonacci(variable)
multiplicando = int(input("Ingrese el número entero: "))
mod_funciones.tabla(multiplicando)
'''
from mod_funciones import * 

def main():
    while True:
        opc = menu()
        match opc:
            case 1:
                print("calcula si un numero es primo")
                valor=int(input("ingrese un numero entero mayor que 1 >> "))
                primo(valor)
            case 2:
                print("imprime la serie de fibonacci")
                num=int(input("ingrese el numero de terminos de la serie de fibonacci >> "))
                fibonacci(num)
            case 3:
                print("imprime la tabla de multiplicar")
                num=int(input("ingrese un numero entero >> "))
                tabla(num)  
            case 4:
                break
            case _:
                print("opcion no valida")


if __name__ == "__main__":
    main()