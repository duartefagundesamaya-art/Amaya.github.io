import cv2
import numpy as np
from detectaCORcopy import segmentar_amarelo

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Erro ao abrir a câmera.")
else:
    # Kernel criado uma vez só, fora do loop
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))

    while True:
        sucesso, imagem = camera.read()

        if not sucesso:
            print("Erro ao capturar a imagem.")
            break

        # 1. Suaviza a imagem
        imagem_filtrada = cv2.GaussianBlur(imagem, (3, 3), 0)

        # 2. Segmenta o amarelo
        mascara = segmentar_amarelo(imagem_filtrada)

        # 3. Fecha buracos (brilho/sombra) e remove ruído
        mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel, iterations=3)
        mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel, iterations=1)

        # 4. Encontra os contornos das bolinhas
        contornos, _ = cv2.findContours(
            mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        resultado = imagem.copy()
        total_bolinhas = 0

        for c in contornos:
            area = cv2.contourArea(c)
            if area < 5:  # ignora ruídos pequenos
                continue

            # Filtra por formato circular
            perimetro = cv2.arcLength(c, True)
            if perimetro == 0:
                continue
            circularidade = 4 * np.pi * area / (perimetro ** 2)
            if circularidade < 0.7:
                continue

            # Círculo que envolve o contorno inteiro
            (x, y), raio = cv2.minEnclosingCircle(c)
            x, y, raio = int(x), int(y), int(raio)

            cv2.circle(resultado, (x, y), raio, (0, 255, 0), 2)
            cv2.circle(resultado, (x, y), 3, (0, 0, 255), -1)
            total_bolinhas += 1

        print("Bolinhas detectadas:", total_bolinhas)

        # 5. Exibe as janelas
        cv2.imshow("Camera original", imagem)
        cv2.imshow("Mascara amarela", mascara)
        cv2.imshow("Resultado", resultado)

        # Pressione Q para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()