control = True

while True:
    print("====================================")
    print("           Menú Principal          ")
    print("====================================")
    print("A. Calcular Sustentación y Arrastre")
    print("B. Calcular Consumo de Combustible")
    print("C. Opción C")
    print("====================================")
    print("Q. Salir")
    print("====================================")

    caso = (input("Introduzca una opción: "))
    caso = caso.upper()

    match caso:
        case "A":
            print("======================================================")
            print("Ha entrado a la calculadora de Sustentación y Arrastre")
            print("======================================================")
            rho = float(input("Ingrese la densidad del aire en kg/m^3: "))
            V = float(input("Ingrese la velocidad del avión en m/s: "))
            S = float(input("Ingrese la superficie alar en m^2: "))
            CL = float(input("Ingrese el coeficiente de sustentación: "))
            CD = float(input("Ingrese el coeficiente de arrastre: "))
            peso = float(input("Ingrese el peso del avión en N: "))
            L = 0.5 * rho * (V**2) * S * CL
            D = 0.5 * rho * (V**2) * S * CD
            print("=============================================")
            print(f"La sustentación del avión son: {L} N")
            print(f"El arrastre del avión son: {D} N")
            if L >= peso:
                print("El avión puede volar.")
            else:
                print("El avión no puede volar.")
            print("=============================================")           
        case "B":
            print("=====================================================")
            print("Ha entrado a la calculadora de Consumo de Combustible")
            print("=====================================================")
            print("A. Cessna 172 Skyhawk")
            print("B. Airbus A320-200")
            print("C. Boeing 737-800")
            print("D. Airbus A380-800")
            print("=======================")
            caso_b = (input("Seleccione una aeronave: "))
            caso_b = caso_b.upper()
            match caso_b:
                case "A":
                    consumo = 30
                    combustible = int(input("Ingrese el combustible en kg: "))
                    tiempo = 0
                    if combustible <= 212:
                        while combustible > 0:
                            tiempo += 1
                            combustible -= consumo
                            if combustible < 0:
                                combustible = 0
                            print(f"Hora {tiempo}: Quedan {combustible} kg")
                        print("========================================")
                        print(f"El C172 Skyhawk voló durante {tiempo} horas.")
                        print("========================================")
                    else:
                        print("Combustible excede la capacidad maxima. Intente una cantidad menor.")
                case "B":
                    consumo = 2300
                    combustible = int(input("Ingrese el combustible en kg: "))
                    tiempo = 0
                    if combustible <= 27200:
                        while combustible > 0:
                            tiempo += 1
                            combustible -= consumo
                            if combustible < 0:
                                combustible = 0
                            print(f"Hora {tiempo}: Quedan {combustible} kg")
                        print("========================================")
                        print(f"El Airbus A320-200 voló durante {tiempo} horas.")
                        print("========================================")
                    else:
                        print("Combustible excede la capacidad maxima. Intente una cantidad menor.")
                case "C":
                    consumo = 3200
                    combustible = int(input("Ingrese el combustible en kg: "))
                    tiempo = 0
                    if combustible <= 26000:
                        while combustible > 0:
                            tiempo += 1
                            combustible -= consumo
                            if combustible < 0:
                                combustible = 0
                            print(f"Hora {tiempo}: Quedan {combustible} kg")
                        print("========================================")
                        print(f"El Boeing 737-800 voló durante {tiempo} horas.")
                        print("========================================")
                    else:
                        print("Combustible excede la capacidad maxima. Intente una cantidad menor.")
                case "D":
                    consumo = 17400
                    combustible = int(input("Ingrese el combustible en kg: "))
                    tiempo = 0
                    if combustible <= 320000:
                        while combustible > 0:
                            tiempo += 1
                            combustible -= consumo
                            if combustible < 0:
                                combustible = 0
                            print(f"Hora {tiempo}: Quedan {combustible} kg")
                        print("========================================")
                        print(f"El Airbus A380-800 voló durante {tiempo} horas.")
                        print("========================================")
                    else:
                        print("Combustible excede la capacidad maxima. Intente una cantidad menor.")
                case _: print("Opción de aeronave invalida.")
        case "C":
            print("Ha seleccionado la opción C.")
        case "Q":
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no valida.")