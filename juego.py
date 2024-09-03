import random

# - Variables globales

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

# - Funciones del juego

def Juego():
    index = random.randint(0, len(palabras)-1)
    palabra = palabras[index]
    palabraSecreta = len(palabra) * "_"
    juego = True
    fallidos = 0
    while juego == True:
        print("\n" * 10)
        print(dibujos[fallidos])
        print("Intentos fallidos:",fallidos,"\n")
        print(palabraSecreta, "\n")
        print(palabra)
        if fallidos == INTENTOS:
            Perdiste(palabra)
        
        seEncuentra = False
        banderaEntrada = True
        while banderaEntrada == True:
            entrada = input("Ingrese una letra o adivine la palabra: ")
            if len(entrada) == 1:
                for i in range(len(palabra)-1):
                    if entrada == palabra[i]:
                        palabraSecreta[i] = palabra[i]
                        seEncuentra = True
                if seEncuentra == False:
                    fallidos += 1
                banderaEntrada = False
            elif len(entrada) > 2:
                if entrada == palabra:
                    juego == False
                else:
                    fallidos = INTENTOS
                banderaEntrada = False
            else:
                print("Intentalo de vuelta.")
            



def Perdiste(palabra):
    band = True
    while band == True:
        print("Perdiste! La palabra era:",palabra,"\nQueres intentar de nuevo? (Y / N)")
        x = input()
        if x == "y":
            band == False
            Juego()
        elif x == "n":
            band == False
        else:
            print("\n" * 10)
            print("Por favor, ingrese una de las 2 opciones que se pidió.")

    
# - Funciones de ingresar una nueva palabra

def IngresarPalabra():
    print("No funca")

#def VerificarPalabra()

# - Funciones de cargar lista de jugadores

def CargarListaJugadores():
    print("No funca")

# - Menu principal

while bandera == True:
    print("\n" * 10)
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