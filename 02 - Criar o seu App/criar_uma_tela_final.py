import sys
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class TelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Meu App')

        botao = QPushButton('Me aperte!')

        self.setFixedSize(QSize(400, 300))  # 1

        self.setCentralWidget(botao)


app = QApplication(sys.argv)

tela = TelaPrincipal()
tela.show()

app.exec_()
