#Calculadora 
'''
control= True #variable buleana

while control == True:
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: ")) 
    print("s. sumar\nR. Restar\nM. Multiplicar\nD. Dividir\nE. Salir")
    opcion=input("Elija una opcion: ")
    match opcion:
        case "S":
            print("SUMA")
            resultado=numero1 + numero2
        case "R":
            print("RESTA")
            resultado=numero1 - numero2
        case "M":
            print("MULTIPLICACION")
            resultado=numero1 * numero2 
        case "D":
            print("DIVISION")
            resultado=numero1 / numero2
        case "E":
            control =False 
    print(f"El resultado es: {resultado}")
'''
'''
control= True #variable buleana

while True:
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: ")) 
    print("s. sumar\nR. Restar\nM. Multiplicar\nD. Dividir\nE. Salir")
    opcion=input("Elija una opcion: ")
    opcion=opcion.upper() #convierte el texto a mayusculas
    match opcion:
        case "S":
            print("SUMA")
            resultado=numero1 + numero2
        case "R":
            print("RESTA")
            resultado=numero1 - numero2
        case "M":
            print("MULTIPLICACION")
            resultado=numero1 * numero2 
        case "D":
            print("DIVISION")
            resultado=numero1 / numero2
        case "E":
            control =False 
    print(f"El resultado es: {resultado}")
'''

control= True #variable buleana

while True:
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: ")) 
    print("s. sumar\nR. Restar\nM. Multiplicar\nD. Dividir\nE. raiz cuadrada\nP Salir")
    opcion=input("Elija una opcion: ")
    opcion=opcion.upper() #convierte el texto a mayusculas
    match opcion:
        case "S":
            print("SUMA")
            resultado=numero1 + numero2
        case "R":
            print("RESTA")
            resultado=numero1 - numero2
        case "M":
            print("MULTIPLICACION")
            resultado=numero1 * numero2 
        case "D":
            print("DIVISION")
            resultado=numero1 / numero2
        case "P":
            print("RAIZ CUADRADA")
            resultado=numero1 ** 0.5
        case "E":
            control =False 
    print(f"El resultado es: {resultado}")

    