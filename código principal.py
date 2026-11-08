# importa a biblioteca do openCV do python 
import cv2
import numpy as np
from detectaCOR import segmentar_amarelo

# carrega a imagem na variável "imagem"
imagem = cv2.imread("./img/imagem.jpeg")


# apenas uma verificação para ver se a imagem foi carregada, para não dar erro na compilação do código 
if imagem is None:
    print("Erro: não foi possível carregar a imagem.")
   

else:
    mascara = segmentar_amarelo(imagem)

    # 2. Limpa a máscara e FECHA os buracos (brilho/sombra das bolinhas)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel, iterations=3)
    mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel, iterations=1)

    # 3. Preenche qualquer buraco interno nos contornos
    contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    resultado = imagem.copy()
    for c in contornos:
        area = cv2.contourArea(c)
        if area < 20:  # ignora ruídos pequenos
            continue

        # Verifica se o formato é aproximadamente circular
        perimetro = cv2.arcLength(c, True)
        circularidade = 4 * np.pi * area / (perimetro ** 2)
        if circularidade < 0.7:
            continue

        # Círculo mínimo que envolve TODO o contorno
        (x, y), raio = cv2.minEnclosingCircle(c)
        x, y, raio = int(x), int(y), int(raio)

        cv2.circle(resultado, (x, y), raio, (0, 255, 0), 2)
        cv2.circle(resultado, (x, y), 3, (0, 0, 255), -1)


  # 6. Exibe os resultados 
    # cv2.namedWindow("Imagem original", cv2.WINDOW_NORMAL)
    # cv2.resizeWindow("Imagem original", 640, 480)
    # cv2.imshow("Imagem original", imagem)


    cv2.namedWindow("Mascara amarela", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Mascara amarela", 640, 480)
    cv2.imshow("Mascara amarela", mascara)

    cv2.namedWindow("Resultado", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Resultado", 640, 480)
    cv2.imshow("Resultado", resultado)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

   





# cv2.namedWindow (esse comando serve para criar uma janela)
# cv2.resizeWindow(esse comando serve para dimensionar o tamanho da janela)
# "./img/imagem.jpeg" (esse é o comando para o algoritmo procurar a imagem dentro da pasta)
# if imagem is None (esse 'none' serve para representar a ausencia de um valor e imprimir a mensagem de erro)
# o cv2.GaussianBlur é o filtro gaussiano, (imagem, (3,3), 0):
# o'imagem', é a imagem de entrada , que foi definida la em cima;
# o '(3,3) é o tamanho do kernel(kernel é basicamente uma matriz de pixel,que nós definimos como 3x3, que vai calcular um novo valor para o pixel central usando uma média ponderada dos pixels vizinhos, no qual os pixels próximos tem amior influencia);
# ja o '0',serve para mandar o openCv2 calcular o sigma da matriz automaticamente, se mudasse o valor de 0para qualquer outro valor, o segma não seria calculado automaticamente, ele seria o numero que colocamos.
# cv2.Canny (funçãodo openCV para detectação de bordas)   
# Cria as janelas com tamanho redimensionável
    # cv2.namedWindow("Minha camera", cv2.WINDOW_NORMAL)
    # cv2.resizeWindow("Minha camera", 640, 480)






