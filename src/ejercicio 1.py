#Calcular el indice de masa corporal de esa persona
#Leer peso y altura
peso = input("ingresa tu peso en KG: ")
peso = float(peso)
altura = input("ingresa tu altura en m: ")
altura = float(altura)
#Calculos
IMC = peso/altura**2
#Mostrar IMC
print("tu IMC = ", IMC)
