import pygame
import time
import pyttsx3
import winsound

ANCHO = 1280
ALTO = 720

partida = 0
puntuacion_totales = 0

NEGRO = (0, 0, 0)
AZUL = (40, 55, 71)
VERDE = (200,200,0)
MARRON = (150, 70, 10)
ROJO = (236, 80, 80)

direccion = ""

prota = pygame.image.load("calavera2.png")


Freq=500

Dur=100

#Mapas

mapa = [
        "XXXXXXXXXXXXXXXX",
        "XaaaaaaaaaaaaaaX",
        "XaaaaaaaaaaaaaaX",
        "XXXXaaXXXXXXXooX",
        "X XXaXXXXeeeeooX",
        "X  eeeeeeeeeXooX",
        "XXXXXXXXXXXXXooX",
        "XXXXXXXXXXXXXFlX",
        "XXXXXXXXXXXXXXXX"
]

mapa1 = [
        "XXXXXXXXXXXXXXXX",
        "XXXoooooo      X",
        "XXXoooXXXXXaX  X",
        "XXXoooXaaaaaXXXX",
        "XXXoXoXXXXXXXXXX",
        "XXXeeeeeeeeeeeeF",
        "XXXXeeXeXXXXXXeX",
        "XXXXeeeeeeeeeeeF",
        "XXXXXXXXXXXXXXXX"
]

mapa2 = [
        "XXXXXXXXXXXXXXXX",
        "XXFlXooooo     X",
        "XXeeXXXXXXXXXXoX",
        "XXeeXaaaaaaaaaaX",
        "XXeeXXaXXXXXXaaX",
        "XXeeeeaaaaaaaaaX",
        "XXeeXeaaXXXXXXXX",
        "XXeeXeaaaXXXXXXX",
        "XXXXXXXXXXXXXXXX"
]

nave = pygame.Rect(600, 400, 50, 50)
nave_vel_x = 0
nave_vel_y = 0

#funciones

#Crear objetos

def dibujar_muro(superficie, rectangulo):
    pygame.draw.rect(superficie, AZUL, rectangulo)

def dibujar_checkpoint(superficie, rectangulo):
    pygame.draw.rect(superficie, ROJO, rectangulo)

def dibujar_camino(superficie, rectangulo):
    pygame.draw.rect(superficie, NEGRO, rectangulo)

#Construccion del mapa y cambio de mapa

def construir_mapa(mapa):
    muros = []
    checkpoints = []
    caminos = []
    segundo_caminos = []
    tercer_caminos = []
    cuarto_caminos = []
    x = 0
    y = 0
    for fila in mapa:
        for baldosa in fila:
            if baldosa == "X":
                muros.append(pygame.Rect(x, y, 80, 80))
            if baldosa == "F":
                checkpoints.append(pygame.Rect(x, y, 160, 80))
            if baldosa == "e":
                caminos.append(pygame.Rect(x, y, 80, 80))
            if baldosa == "a":
                segundo_caminos.append(pygame.Rect(x, y, 80, 80))
            if baldosa == "o":
                tercer_caminos.append(pygame.Rect(x, y, 80, 80))
            if baldosa == " ":
                cuarto_caminos.append(pygame.Rect(x, y, 80, 80))
            x += 80
        x = 0
        y += 80

    return muros, checkpoints, caminos, segundo_caminos, tercer_caminos, cuarto_caminos


def dibujar_mapa(superficie, muros, checkpoints, caminos, segundo_caminos, tercer_caminos, cuarto_caminos):
    for muro in muros:
        dibujar_muro(superficie, muro)

    for checkpoint in checkpoints:
        dibujar_checkpoint(superficie, checkpoint)

    for camino in caminos:
        dibujar_camino(superficie, camino)

    for segundo_camino in segundo_caminos:
        dibujar_camino(superficie, segundo_camino)

    for tercer_camino in tercer_caminos:
        dibujar_camino(superficie, tercer_camino)

    for cuarto_camino in cuarto_caminos:
        dibujar_camino(superficie, cuarto_camino)

def cambio_de_mapa(partida, mapa):

    if partida == 0:
        txt="La salida se encuentra en la esquina inferior derecha del mapa, tu comienzas en el lado izquierdo del mapa en la mitad del mapa"
        convertir_texto(txt)
        muros, checkpoints, caminos, segundo_caminos, tercer_caminos, cuarto_caminos = construir_mapa(mapa)
        nave.x = 100
        nave.y = 330
        start = time.time()
        ayudas = 0
        return muros, checkpoints, caminos, segundo_caminos, tercer_caminos, cuarto_caminos, nave.x, nave.y, start, ayudas



    if partida == 1:
            txt="La salida se encuentra en la esquina inferior derecha del mapa, tu comienzas en la esquina superior derecha del mapa"
            convertir_texto(txt)
            muros, checkpoints, caminos, segundo_caminos, tercer_caminos, cuarto_caminos = construir_mapa(mapa1)
            nave.x = 1080
            nave.y = 170
            start = time.time()
            ayudas = 0
            return muros, checkpoints, caminos, segundo_caminos, tercer_caminos, cuarto_caminos, nave.x, nave.y, start, ayudas



    if partida == 2:
            txt="La salida se encuentra en la esquina superior izquierda del mapa, tu comienzas en la esquina superior derecha del mapa"
            convertir_texto(txt)
            muros, checkpoints, caminos, segundo_caminos, tercer_caminos, cuarto_caminos = construir_mapa(mapa2)
            nave.x = 1140
            nave.y = 90
            start = time.time()
            ayudas = 0
            return muros, checkpoints, caminos, segundo_caminos, tercer_caminos, cuarto_caminos, nave.x, nave.y, start, ayudas



#Salida de audio

def convertir_texto(archivo_de_texto):
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    leer = pyttsx3.init()
    try:
        o = open(archivo_de_texto,"r")
        lineas = o.readlines()
        texto = lineas
        leer.say(texto)
        o.close()

    except:
        leer.say(archivo_de_texto)
    leer.runAndWait()


#Puntuacion y ayudas

def calcular_puntuacion(tiempo, puntuacion_total):
    puntos = 0
    if tiempo <= 60:
        puntos = 3
        puntuacion_total += 3
    if tiempo > 60 and tiempo <= 120:
        puntos = 2
        puntuacion_total += 2
    if tiempo > 120:
        puntos = 1
        puntuacion_total += 1
    puntuacion = "Ha terminado el nivel con", puntos, "estrellas"
    return puntuacion, puntuacion_total

def ayuda_camino_e(ayudas, partida, caminos):
     for camino in caminos:

        if nave.colliderect(camino):

        #Primer mapa

            if ayudas == 1 and partida == 0:
                txt = "Estas cerca de la salida, para llegar a ella dirigete hacia la derecha"
                convertir_texto(txt)
                return

            if ayudas == 2 and partida == 0:
                txt = "Hay un obstaculo entre tu y la salida"
                convertir_texto(txt)
                return

            if ayudas == 3 and partida == 0:
                txt = "Recuerda que la salida se encuentra en la esquina derecha del laberinto"
                convertir_texto(txt)
                return

            #PSegundo mapa

            if ayudas == 1 and partida == 1:
                txt = "La salida se encuentra en la esquina derecha del mapa, ve hacia abajo"
                convertir_texto(txt)
                return

            if ayudas == 2 and partida == 1:
                txt = "Estas cerca de la salida, puedes guiarte con los obstaculos cercanos"
                convertir_texto(txt)
                return

            if ayudas == 3 and partida == 1:
                txt = "En este mapa tienes dos salidas, debes moverte horizontalmente para encontrarlas"
                convertir_texto(txt)
                return


            #Tercer mapa

            if ayudas == 1 and partida == 2:
                txt = "Estas a pocos pasos de la salida, pero tienes obstaculos en medio"
                convertir_texto(txt)
                return

            if ayudas == 2 and partida == 2:
                txt = "Para llegar a la salida, debes ir hacia arriba, puedes guiarte con las paredes"
                convertir_texto(txt)
                return

            if ayudas == 3 and partida == 2:
                txt = "Recuerda que la salida se encuentra en la equina izquierda del laberinto"
                convertir_texto(txt)
                return

            #Ayudas agotadas
            if ayudas > 3:
                txt = "Ya no tienes mas ayudas"
                convertir_texto(txt)
                return



def ayuda_camino_a(ayudas, partida, segundo_caminos):
    for segundo_camino in segundo_caminos:

        if nave.colliderect(segundo_camino):

        #Primer mapa

            if ayudas == 1 and partida == 0:
                txt = "Te encuentras del lado opuesto a la salida"
                convertir_texto(txt)
                return

            if ayudas == 2 and partida == 0:
                txt = "Para llegar a la salida tienes que ir hacia abajo"
                convertir_texto(txt)
                return

            if ayudas == 3 and partida == 0:
                txt = "Guiate con los obstaculos, recuerda que la salida esta del lado inferior del laberinto, tu estas en el superior"
                convertir_texto(txt)
                return

            #PSegundo mapa

            if ayudas == 1 and partida == 1:
                txt = "Te encuentras atrapado, guiate con las paredes de tu alrededor"
                convertir_texto(txt)
                return

            if ayudas == 2 and partida == 1:
                txt = "Para salir de donde estas ve hacia arriba"
                convertir_texto(txt)
                return

            if ayudas == 3 and partida == 1:
                txt = "Para salir de este callejon, debes dirigirte hacia la derecha, y luego hacia arriba"
                convertir_texto(txt)
                return


            #Tercer mapa

            if ayudas == 1 and partida == 2:
                txt = "La salida se encuentra en diagonal, pero tienes obstaculos en medio"
                convertir_texto(txt)
                return

            if ayudas == 2 and partida == 2:
                txt = "Dirigete hacia la izquierda y guiate con las paredes para encontrar la salida"
                convertir_texto(txt)
                return

            if ayudas == 3 and partida == 2:
                txt = "Recuerda que la salida se encuentra en la esquina izquierda del laberinto"
                convertir_texto(txt)
                return

            #Ayudas agotadas
            if ayudas > 3:
                txt = "Ya no tienes mas ayudas"
                convertir_texto(txt)
                return


def ayuda_camino_o(ayudas, partida, tercer_caminos):
    for tercer_camino in tercer_caminos:

        if nave.colliderect(tercer_camino):
            #Primer Mapa
            if partida == 0 and ayudas < 4:
                txt = "Ve hacia abajo para llegar a la salida"
                convertir_texto(txt)
                return
            #Segundo Mapa

            if partida == 1 and ayudas == 1:
                txt = "A tu izquierda tienes una pared, usala para guiarte"
                convertir_texto(txt)
                return

            if partida == 1 and ayudas == 2:
                txt = "Las salidas se encuentran en la esquina derecha de la pantalla"
                convertir_texto(txt)
                return

            if partida == 1 and ayudas == 3:
                txt = "Este laberinto tiene dos salidas, estas se encuentran hacia abajo y hacia la derecha de ti"
                convertir_texto(txt)
                return

            #Tercer Mapa

            if partida == 2 and ayudas <= 3:
                txt = "Si estas atrapado ve hacia la derecha y hacia abajo"
                convertir_texto(txt)
                return

            #Ayudas agotadas
            if ayudas > 3:
                txt = "Ya no tienes mas ayudas"
                convertir_texto(txt)
                return


def ayuda_camino(ayudas, partida, cuarto_caminos):
    for cuarto_camino in cuarto_caminos:
        if nave.colliderect(cuarto_camino):
            txt = "Estas muy cerca de el comienzo, en esta zona no puedes pedir una ayuda"
            return





