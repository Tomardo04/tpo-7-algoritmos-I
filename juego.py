import random

# Variables globales

INTENTOS = 6
palabras = ["Variable", "Función", "Algoritmo","Depuración", "Compilador", "Objeto"]
bandera = True
dibujos = [
    '''
       +---+
       |   |
           |
           |
           |
           |
    =========
    ''', 
    '''
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    ''',
    '''
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    '''
]

# Funciones del juego

def Juego():
    index = random.randint(0, len(palabras)-1)
    palabra = palabras[index]
    palabraSecreta = len(palabra) * ". "
    print(palabraSecreta)
    

    
# Funciones de ingresar una nueva palabra

def IngresarPalabra():
    print("No funca")

# Funciones de cargar lista de jugadores

def CargarListaJugadores():
    print("No funca")

# Menu principal

while bandera == True:
    print("  ___   _   _ ___________  _____   ___ ______ _____ \n / _ \ | | | |  _  | ___ \/  __ \ / _ \|  _  \  _  | \n/ /_\ \| |_| | | | | |_/ /| /  \// /_\ \ | | | | | | \n|  _  ||  _  | | | |    / | |    |  _  | | | | | | |\n| | | || | | \ \_/ / |\ \ | \__/\| | | | |/ /\ \_/ /\n\_| |_/\_| |_/\___/\_| \_| \____/\_| |_/___/  \___/\n----------------------------------------------------")
    print("1 - Empezar nuevo juego")
    print("2 - Agregar palabra")
    print("3 - Lista histórica de jugadores")
    print("4 - Salir\n----------------------------------------------------")
    x = int(input("Ingrese el número de la opción que quiere elegir: "))
    if x == 1:
        Juego()
    elif x == 2:
        IngresarPalabra()
    elif x == 3:
        CargarListaJugadores()
    elif x == 4:
        bandera = False
        print("Saliste del juego")
    else:
        print("Entrada invalida")