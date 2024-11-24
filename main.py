from laberinto import *


def main():

    matriz = generar_matriz_inicial()

    laberinto = generar_laberinto(0, 0, matriz)

    laberinto = generar_ES(laberinto)

    mostrar_laberinto(laberinto)


main()
