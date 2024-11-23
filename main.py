def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])


def generar_size_laberinto(entrada, salida):
    posibles_nums = entrada + salida
    return max(posibles_nums) + 1


def generar_matriz_laberinto(entrada, salida, size):
    matriz = []

    for i in range(size):
        fila = []

        for j in range(size):
            if i == entrada[0] and j == entrada[1]:
                fila.append("P")
            elif i == salida[0] and j == salida[1]:
                fila.append("S")
            else:
                fila.append("")

        matriz.append(fila)
    return matriz


def main():

    entrada = [1, 3]
    salida = [2, 8]

    # entrada = input("Ingrese la coordenada de entrada: ")
    # salida = input("Ingrese la coordenada de salida: ")

    # entrada = entrada.split(",")
    # salida = salida.split(",")

    # entrada = (int(entrada[0]), int(entrada[1]))
    # salida = (int(salida[0]), int(salida[1]))

    tam_lab = generar_size_laberinto(entrada, salida)

    matriz_lab = generar_matriz_laberinto(entrada, salida, tam_lab)

    # mostrar_matriz(matriz_lab)


main()
