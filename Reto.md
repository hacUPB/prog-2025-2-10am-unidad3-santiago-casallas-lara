Problema 1 - Calculadora de Sustentación y Arrastre
Descripción del problema
Este programa permite al usuario calcular la sustentación y el arrastre de una aeronave al ingresar datos necesarios para calcular esto, como Densidad del Aire, Velocidad del Avión, Superficie Alar, Coeficiente de Sustentación y Arrastre y peso de la aeronave. Se utilizan estas variables para calcular la sustentación y el arrastre con las fórmulas respectivas de estos dos donde se relacionan todas las variables, para finalmente mostrarle al usuario estos valores y si el avión es apto para volar, teniendo en cuenta si la sustentación es mayor al peso. Si la sustentación es menor al peso, el programa le dice al usuario que la aeronave no es apta para volar.

Análisis
Variables de entrada:

rho
V
S
CL
CD
Peso
Variables de Salida:

L
D
Pseudocódigo
Inicio
Escribir "Ha entrado a la calculadora de sustentación y arrastre"
Leer rho, V, S, CL, CD, Peso
L = 0.5 * rho * ( V^2 ) * S * CL
D = 0.5 * rho * ( V^2 ) * S * CD
Mostrar L, D
Si L >= Peso
  Escribir "El avion puede volar"
Sino
  Escribir "El avion no puede volar"
Fin si
Fin

Problema 2 - Calculadora de Horas de Vuelo según Combustible
Descripción del problema
Se le presenta un menú al usuario con cuatro opciones de aeronaves para elegir, que varían desde un Cessna 172 Skyhawk hasta un Airbus A380-800, las cuales funcionan con los datos reales de consumo de combustible y de capacidad de combustible. Se le pide al usuario ingresar una cantidad de combustible en KG; si la cantidad es mayor a la capacidad de la aeronave, se repite la pregunta hasta que se ingrese un valor permitido. Al ingresar el valor, el programa muestra cuantas horas de vuelo han pasado y cuanto combustible resta hasta que la aeronave agote el combustible, mostrando finalmente, en modo de resumen, cuantas horas voló la aeronave.

Análisis
Variables de entrada:

caso_b
combustible
Variables de control:

tiempo
consumo
Variables de Salida:

combustible
tiempo
Pseudocódigo
Inicio
Escribir "Ha entrado a la calculadora de Consumo de Combustible"
Leer caso_b
Match caso_b
  Case "A":
    consumo = 30
    Leer combustible
    tiempo = 0
    Si combustible <= 212
      Mientras combustible > 0
        tiempo = tiempo + 1
        combustible = combustible - consumo
        Si Combustible < 0
          combustible = 0
        Fin si
        Mostrar tiempo, combustible
      Fin mientras
    Mostrar tiempo
    Sino
      Escribir "Combustible excede la capacidad maxima. Intente una cantidad menor."
    Fin si
  Case "B":
    consumo = 2300
    Leer combustible
    tiempo = 0
    Si combustible <= 27200
      Mientras combustible > 0
        tiempo = tiempo + 1
        combustible = combustible - consumo
        Si Combustible < 0
          combustible = 0
        Fin si
        Mostrar tiempo, combustible
      Fin mientras
    Mostrar tiempo
    Sino
      Escribir "Combustible excede la capacidad maxima. Intente una cantidad menor."
    Fin si
  Case "C":
    consumo = 3200
    Leer combustible
    tiempo = 0
    Si combustible <= 26000
      Mientras combustible > 0
        tiempo = tiempo + 1
        combustible = combustible - consumo
        Si Combustible < 0
          combustible = 0
        Fin si
        Mostrar tiempo, combustible
      Fin mientras
    Mostrar tiempo
    Sino
      Escribir "Combustible excede la capacidad maxima. Intente una cantidad menor."
    Fin si
  Case "D":
    consumo = 17400
    Leer combustible
    tiempo = 0
    Si combustible <= 320000
      Mientras combustible > 0
        tiempo = tiempo + 1
        combustible = combustible - consumo
        Si Combustible < 0
          combustible = 0
        Fin Si
        Mostrar tiempo, combustible
      Fin Mientras
    Mostrar tiempo
    Sino
      Escribir "Combustible excede la capacidad maxima. Intente una cantidad menor."
    Fin Si
  Case _:
    Escribir "Opcion de aeronave invalida"
Fin

Problema 3 - Simulador de Abordaje de un Airbus A330
Descripción del problema
Este programa permite al usuario simular el abordaje de una aeronave, más concretamente un Airbus A330-300, con capacidad para 290 pasajeros, número que se utiliza como límite en este código. Se le pide al usuario ingresar una cantidad de pasajeros estrictamente menor o igual a 290, y en múltiplos de 10; el programa detecta si uno o ambos requisitos no se cumplen, y vuelve a formular la pregunta hasta que se ingresen valores permitidos. Se necesitan numeros multiplos de 10 para poder dividir el numero de personas en 5 grupos de abordaje, pues es imposible que una persona aparezca como numero decimal. Se le muestra al usuario que grupo empieza a abordar, cuantos abordan y cuando termina el abordaje de cada grupo, pasando por todos los pasajeros. Finalmente, como modo de resumen se muestra cuantos pasajeros abordaron el vuelo correctamente.

Análisis
Variables de entrada:

Pasajeros
Variables de control:

i
tamaño_grupo
grupo
pasajero_Actual
Variables de Salida:

pasajeros
Pseudocódigo
Escribir "Ha entrado al Simulador de Abordaje"
Escribir "La aeronave es un A330-300 - Capacidad Maxima: 290 pasajeros."
Leer pasajeros
Mientras pasajeros > 290
  Escribir "Cantidad maxima excedida, ingrese un numero menor."
  Leer pasajeros
Fin Mientras
Mientras pasajeros % 10 != 0
  Escribir "Ingrese una cantidad en multiplos de 10"
  Leer pasajeros
Fin Mientras
tamaño_grupo = pasajeros / 5
Escribir tamaño_grupo
pasajero_actual = 1
grupo = 1
Mientras pasajero_actual <= pasajeros
  Escribir grupo
  Para i desde 1 hasta tamaño_grupo
    Si pasajero_actual <= pasajeros
      Escribir pasajero_actual
      pasajero_actual = pasajero_actual + 1
    Fin Si
  Fin Para
  Escribir grupo
  grupo = grupo + 1
Fin Mientras
Mostrar pasajeros
Fin