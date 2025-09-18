'''
#Crea un programa que convierta temperaturas entre Celsius y Fahrenheit. El programa debe:

1. Preguntar al usuario si desea convertir de Celsius a Fahrenheit (ingresando 'C') o de Fahrenheit a Celsius (ingresando 'F')
2. Aceptar un valor de temperatura como entrada
3. Realizar la conversión usando la fórmula apropiada
4. Continuar pidiendo conversiones hasta que el usuario ingrese 'Q' para salir

**Entrada:** Un carácter ('C', 'F', o 'Q') y un valor numérico de temperatura
**Salida:** El valor de temperatura convertido con las unidades correspondientes
'''
'''
Variables de entrada 
nombre          tipo 
opcion          str
temperatura     float 

Variables de salida 
Nombre          tipo 
Conversion      float   

Variable de control
opcion
'''

opcion= 'F'    #Asigno un valor diferente de Q
while opcion != 'Q':
    opcion =input("F. Fahrenheit a Celsius\nC. celsius a fahrenheit\nQ. Salir\n")
    opcion = opcion.upper()
    if opcion != 'Q':

        temperatura = float(input("ingrese la temperatura a convertir: "))
        match opcion:
            case 'F':
                conversion = (temperatura - 32) *(5/9)
                print(f"{temperatura}°F = {conversion}°C")
            case 'C':
                conversion = (temperatura * 9/5)+32
                print(f"{temperatura}°C = {conversion}°F")
            case 'Q':
                print("saliendo del programa...")
            case _:
                print("opcion no valida")