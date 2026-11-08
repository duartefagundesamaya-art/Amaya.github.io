import cv2
import numpy as np


#função para fazer a segmentação por cor
# ele recebe a imagem vinda do arquivo 'kk.py' por parametro, para fazer a modificação e retornar com o filtro j
def segmentar_amarelo(imagem):


    #essa linha vai converter a imagem de RGB para HSV para conseguir passar a segmentação por cor
    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

    ''' essas duas linhas de amarelo_min e amarelo_
    max faz com o modelo do hsv detecte desde amarelo mais claros e menos saturados 
        até amarelos mais escuros e mais saturados'''

    amarelo_min = np.array([20, 80, 100])
 
    amarelo_max = np.array([40, 255, 255])
                     #      |    |    |_V
                          # |    |______S               
                          # |___________H



    #cria a mascara, ou seja, essa linha é o que faz com que os itens amarelos virem brancos, quando mostrado na tela 
    mascara = cv2.inRange(
        hsv,
        amarelo_min,
        amarelo_max
    )

# esse return serve para mandar para o 'kk.py' o resultado da imagem com a segmentação
    return mascara




#   H S V-value(valor)
#   | |______Saturação
#   |________Matriz
#  o HSV é um modelo de representação das cores que detecta as cores a partir desses tês valores(matriz, saturação e valor do brilho)
