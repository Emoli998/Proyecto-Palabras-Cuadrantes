def validar_palabra():

    palabra = input("Ingresa una palabra: ")

    # Creamos una lista vacía para almacenar todos los intentos.
    historial_palabras = []

    # Guardamos el primer intento en la lista.
    historial_palabras.append(palabra)

    while len(palabra) < 4 or len(palabra) > 8:

        if len(palabra) < 4:
            print("!Hacen falta letras!")

        else:
            print("!Sobran letras!")

        palabra = input("Intenta nuevamente: ")

        # Agregamos cada nuevo intento al historial.
        historial_palabras.append(palabra)

    print("Palabra correcta")
    print("Historial de intentos:", historial_palabras)

def solicitar_coordenada():

    while True:

        try:
            x = float(input("Ingresa una coordenada: "))

            if x == 0:
                print("El cero no es válido para esta coordenada.")
                continue

            return x

        except ValueError:
            print("Vuelve a intentarlo, pero esta vez con un número :p")

def determinar_cuadrante():

    # Tupla que almacena los nombres de los cuatro cuadrantes.
    # Cada cuadrante tiene un índice que comienza desde cero.
    cuadrantes = (
        "Cuadrante I",    # Índice 0
        "Cuadrante II",   # Índice 1
        "Cuadrante III",  # Índice 2
        "Cuadrante IV"    # Índice 3
    )

 # Obtenemos las coordenadas mediante nuestra función.
    x = solicitar_coordenada()
    y = solicitar_coordenada()


    # Identificamos el cuadrante mediante el índice correspondiente.
    if x > 0 and y > 0:
        indice = 0

    elif x < 0 and y > 0:
        indice = 1

    elif x < 0 and y < 0:
        indice = 2

    elif x > 0 and y < 0:
        indice = 3

    # Consultamos la tupla utilizando el índice obtenido.
    print("Se encuentra en el", cuadrantes[indice])


# Ejecutamos las dos funciones.
validar_palabra()
determinar_cuadrante()