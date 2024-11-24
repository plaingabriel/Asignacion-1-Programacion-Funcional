from create_wall import create_wall


def generar_matriz_inicial():
    size_matriz = int(input("Ingrese el tamaño del laberinto: "))

    if size_matriz < 6:
        print("El laberinto debe tener al menos seis filas y cinco columnas")
        return generar_matriz_inicial()

    matriz = []

    for i in range(size_matriz - 1):
        matriz.append([" " for i in range(size_matriz)])

    return matriz


def mostrar_laberinto(matriz):
    for i in range(len(matriz)):
        print(matriz[i])


def generar_laberinto(fil, col, matriz):
    # Fill the first row
    if fil == 0 and col < len(matriz[fil]):
        matriz[fil][col] = "*"

        return generar_laberinto(fil, col + 1, matriz)

    # Change to the next row
    elif fil < len(matriz) and col == len(matriz[fil]):

        return generar_laberinto(fil + 1, 0, matriz)

    # Fill the last column
    elif fil < len(matriz) and col == len(matriz[fil]) - 1:
        matriz[fil][col] = "*"

        return generar_laberinto(fil, col + 1, matriz)

    # Fill the first column
    elif fil < len(matriz) and col == 0:
        matriz[fil][col] = "*"

        return generar_laberinto(fil, col + 1, matriz)

    # Fill the last row
    elif fil == len(matriz) - 1 and col < len(matriz[fil]):
        matriz[fil][col] = "*"

        return generar_laberinto(fil, col + 1, matriz)

    # Fill the other cells
    elif fil < len(matriz) and col < len(matriz[fil]):
        matriz[fil][col] = create_wall()

        return generar_laberinto(fil, col + 1, matriz)

    return matriz


def generar_ES(laberinto):

    limites = [len(laberinto) - 1, len(laberinto[0]) - 1]
    bandera = 1

    while bandera == 1:
        entrada = input("Ingrese la coordenada de entrada: ").split(",")
        entrada = [int(entrada[0]), int(entrada[1])]

        salida = input("Ingrese la coordenada de salida: ").split(",")
        salida = [int(salida[0]), int(salida[1])]

        # entrada = [1, 3]
        # salida = [2, 8]

        if (
            entrada[0] > limites[0]
            or entrada[1] > limites[1]
            or salida[0] > limites[0]
            or salida[1] > limites[1]
        ):
            print("Las coordenadas deben estar dentro del laberinto")
        elif entrada == salida:
            print("Las coordenadas de entrada y salida deben ser diferentes")

        # Asegurarse que la coordenada de salida debe estar en algún borde del laberinto
        elif (salida[1] != 0 and salida[1] != limites[1]) and (
            salida[0] != 0 and salida[0] != limites[0]
        ):
            print("La coordenada de salida debe estar en algún borde del laberinto")

        else:
            bandera = 0

    laberinto[entrada[0]][entrada[1]] = "E"

    laberinto[salida[0]][salida[1]] = "S"

    return laberinto
