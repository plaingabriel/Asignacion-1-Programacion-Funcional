from create_wall import create_wall


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


def main():

    entrada = [1, 3]
    salida = [2, 8]

    # entrada = input("Ingrese la coordenada de entrada: ")

    # entrada = entrada.split(",")

    # entrada = (int(entrada[0]), int(entrada[1]))

    matriz = [
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " "],
    ]

    laberinto = generar_laberinto(0, 0, matriz)

    mostrar_laberinto(laberinto)


main()
