import random
import string as str
import re

# - Variables globales

INTENTOS = 6
palabras = ["variable", "funcion", "algoritmo","depuracion", "compilador", "objeto", "computadora", "juego", "string", "random", "mouse", "teclado", "python", "javascript", "chrome", "facultad", "clase", "aula", "memoria", "procesador", "almacenamiento", "impresora", ""]
bandera = True
ganaste = False
perdiste = False
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

# - Funciones globales

def VerificarPalabra(palabra):
    if re.match("^[a-zA-Z]+$", palabra):
        return True
    else:
        return False

# - Funciones del juego

def Juego():
    index = random.randint(0, len(palabras)-1)
    palabra = palabras[index]
    palabraSecreta = len(palabra) * "_"
    juego = True
    fallidos = 0
    utilizadas = []
    while juego == True:
        print("\n" * 10)
        print(dibujos[fallidos])
        print("Intentos fallidos:",fallidos,"\n")
        print(palabraSecreta.capitalize(), "\n")
        if len(utilizadas) > 0:
            print("Letras utilizadas:",utilizadas)
        
        if palabraSecreta == palabra:
            Ganaste(palabra)
            juego = False
            break
        if fallidos == INTENTOS:
            Perdiste(palabra)
            juego = False
            break
        
        banderaEntrada = True
        while banderaEntrada == True:
            entrada = input("Ingrese una letra o adivine la palabra: ")
            entrada = entrada.lower()
            if len(entrada) == 1:
                if entrada not in utilizadas:
                    utilizadas.append(entrada)
                    seEncuentra = False
                    for i in range(len(palabra)):
                        if entrada == palabra[i]:
                            palabraSecreta = list(palabraSecreta)
                            palabra = list(palabra)
                            palabraSecreta[i] = palabra[i]
                            palabraSecreta = "".join(palabraSecreta)
                            palabra = "".join(palabra)
                            seEncuentra = True
                    if seEncuentra == False:
                        fallidos += 1
                banderaEntrada = False
            elif len(entrada) > 2:
                if VerificarPalabra(entrada) == True:
                    if entrada == palabra:
                        Ganaste(palabra)
                        juego = False
                    else:
                        fallidos = INTENTOS
                    banderaEntrada = False
                else:
                    print("Intente con una palabra válida")
            else:
                print("Intentalo de vuelta")
            

def Perdiste(palabra):
    print("Perdiste! La palabra correcta era:", palabra.capitalize(),"\nPresiona Enter para continuar")
    x = input()

def Ganaste(palabra):
    print("Felicitaciones! La palabra era:", palabra.capitalize(),"\nPresiona Enter para continuar")
    x = input()
    
# - Funciones de gestion de palabras

def IngresarPalabra():
    band = True
    while band == True:
        x = input("Ingrese una palabra de 3 caracteres o más que quiera agregar (Presione Enter para salir): ")
        if len(x) == 0:
            band = False
        elif len(x) > 2:
            x = x.lower()
            if VerificarPalabra(x) == True and x not in palabras:
                palabras.append(x)
                print("Se ha ingresado una nueva palabra:", x.capitalize())
            else:
                print("Ingrese una palabra válida")
        else:
            print("Intentalo de vuelta")

def EliminarPalabra():
    band = True
    while band == True:
        print(palabras)
        x = input("Ingrese una palabra que quiera eliminar (Presione Enter para salir): ")
        if len(x) == 0:
            band = False
        elif len(x) > 2:
            x = x.lower()
            if VerificarPalabra(x) == True and x in palabras:
                palabras.remove(x)
                print("Se ha eliminado una palabra:", x.capitalize())
            else:
                print("Ingrese una palabra válida")
        else:
            print("Intentalo de vuelta")

# - Funciones de gestion de jugadores

def GuardarPartida():
    print("No funca")

def ListaDeJugadores():
    print("No funca")

# - Menu principal

while bandera == True:
    print("\n" * 10)
    print("  ___   _   _ ___________  _____   ___ ______ _____ \n / _ \ | | | |  _  | ___ \/  __ \ / _ \|  _  \  _  | \n/ /_\ \| |_| | | | | |_/ /| /  \// /_\ \ | | | | | | \n|  _  ||  _  | | | |    / | |    |  _  | | | | | | |\n| | | || | | \ \_/ / |\ \ | \__/\| | | | |/ /\ \_/ /\n\_| |_/\_| |_/\___/\_| \_| \____/\_| |_/___/  \___/\n\nBy Tomás B., alumno UADE\n----------------------------------------------------")
    print("1 - Empezar nuevo juego")
    print("2 - Agregar palabra")
    print("3 - Eliminar palabra")
    print("4 - Guardar partida")
    print("5 - Lista histórica de jugadores")
    print("6 - Salir\n----------------------------------------------------")
    x = int(input("Ingrese el número de la opción que quiere elegir: "))
    if x == 1:
        Juego()
    elif x == 2:
        IngresarPalabra()
    elif x == 3:
        EliminarPalabra()
    elif x == 4:
        GuardarPartida()
    elif x == 5:
        ListaDeJugadores()
    elif x == 6:
        bandera = False
        print("Saliste del juego")
    else:
        print("Entrada invalida")