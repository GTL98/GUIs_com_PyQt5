import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton  # 1


# Subclasse QMainWindow para personalizar a tela principal do seu aplicativo
class TelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()  # 2

        self.setWindowTitle('Meu App')

        botao = QPushButton('Me aperte!')

        # Definir o widget central da tela
        self.setCentralWidget(botao)  # 3


app = QApplication(sys.argv)

tela = TelaPrincipal()
tela.show()

app.exec_()
