import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Meu App')

        self.botao = QPushButton('Me aperte!')  # 1
        self.botao.clicked.connect(self.botao_clicado)

        self.setCentralWidget(self.botao)

    def botao_clicado(self):
        self.botao.setText('Você já me clicou')  # 2
        self.botao.setEnabled(False)  # 3

        # Mudar o título da janela
        self.setWindowTitle('Meu App de tiro único')


app = QApplication(sys.argv)

janela = JanelaPrincipal()
janela.show()

app.exec_()
