from modulos.mod_funciones import *

def main():
	control = True
	while True:
		print("======================================")
		print("            Menú Principal           ")
		print("======================================")
		print("A. Calcular Sustentación y Arrastre")
		print("B. Calcular Consumo de Combustible")
		print("C. Simular el Abordaje a una Aeronave")
		print("======================================")
		print("Q. Salir")
		print("======================================")

		caso = (input("Introduzca una opción: "))
		caso = caso.upper()

		match caso:
			case "A":
				caso_a()
			case "B":
				caso_b()
			case "C":
				caso_c()
			case "Q":
				print("Saliendo del programa...")
				break
			case _:
				print("Opción no valida.")

if __name__ == "__main__":
    main()