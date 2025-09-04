#determinar si un numero es par o impar 
numero = int(input ("ingresa un numero: "))
residuo = numero % 2
#si residuo es par 
if residuo == 0:
    print(numero, "es par")
else:
    print(numero, "es impar")
#fin del programa 