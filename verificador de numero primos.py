'''
Implementa un programa que determine si un número es primo y, en caso de no serlo, muestre sus factores. El programa debe:

1. Solicitar al usuario un número entero positivo mayor que 1
2. Determinar si el número es primo
3. Si no es primo, mostrar todos sus factores
4. Permitir al usuario verificar múltiples números

**Entrada:** Un número entero positivo
**Salida:** Mensaje indicando si el número es primo o no, y sus factores si corresponde
'''
'''
Variables de entrada 
nombre          tipo
numero          int

variables de salida
divisores      
'''
numero = int(input("ingrese un numero entero positivo mayor que 1: "))
for i in range(1, numero + 1):
    if numero % i == 0:
        cont += 1 #contador es igual a contador mas 1
    
if cont == 2:
        print(f"{numero} es primo")
else:
     print(f"los divisores de {numero} son: ")
     for i in range(1, numero + 1):
         if numero % i == 0:
            print(i) 