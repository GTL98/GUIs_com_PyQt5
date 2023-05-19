import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Meu App')

        widget = QLabel('Olá')
        widget.setPixmap(QPixmap('dna.jpg'))
        widget.setScaledContents(True)

        self.setCentralWidget(widget)


app = QApplication(sys.argv)

janela = JanelaPrincipal()
janela.show()

app.exec_()
