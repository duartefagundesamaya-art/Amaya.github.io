import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import cv2

class ImageWindow(QMainWindow):
    def __init__(self, image_path: str):
        super().__init__()
        self.setWindowTitle("Visualizador de Imagem")
        self.resize(800, 600)

        label = QLabel(self)
        pixmap = QPixmap(image_path)

        # Configura a imagem para ajustar à janela mantendo a proporção
        label.setPixmap(pixmap)
        label.setScaledContents(False)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    
    # Substitua pelo caminho da sua imagem (PNG, JPG, etc.)
    caminho_imagem = "../img/imagem.jpeg"

    cv2.namedWindow("Visualizador de Imagem", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Imagem original", 640, 480)
    janela = ImageWindow(caminho_imagem)
    janela.show()
    
    sys.exit(app.exec())