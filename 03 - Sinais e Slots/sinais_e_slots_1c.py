import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.botao_esta_alterado = True  # 1

        self.setWindowTitle('Meu App')

        botao = QPushButton('Me aperte!')
        botao.setCheckable(True)
        botao.clicked.connect(self.botao_alterado)
        botao.setChecked(self.botao_esta_alterado)  # 2

        self.setCentralWidget(botao)

    def botao_alterado(self, verificacao):
        self.botao_esta_alterado = verificacao
        print(self.botao_esta_alterado)  # 3


app = QApplication(sys.argv)

janela = JanelaPrincipal()
janela.show()

app.exec_()
