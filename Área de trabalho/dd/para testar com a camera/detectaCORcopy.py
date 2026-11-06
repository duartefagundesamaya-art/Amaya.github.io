
import cv2
import numpy as np

def segmentar_amarelo(camera):
    # Converte a imagem de BGR para HSV
    hsv = cv2.cvtColor(camera, cv2.COLOR_BGR2HSV)

    #usa o 'amarelo_min' para detectar regi
    amarelo_min = np.array([20, 80, 100])
    amarelo_max = np.array([40, 255, 255])

    # Cria a máscara das regiões amarelas
    mascara = cv2.inRange(
        hsv,
        amarelo_min,
        amarelo_max
    )

    return mascara
