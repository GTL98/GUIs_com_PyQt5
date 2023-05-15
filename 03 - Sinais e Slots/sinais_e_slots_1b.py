import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Meu App')

        botao = QPushButton('Me aperte!')
        botao.setCheckable(True)
        botao.clicked.connect(self.botao_clicado)
        botao.clicked.connect(self.botao_alterado)

        self.setCentralWidget(botao)

    def botao_clicado(self):
        print('Clicado!')

    def botao_alterado(self, verificacao):
        print('Verificado?', verificacao)


app = QApplication(sys.argv)

janela = JanelaPrincipal()
janela.show()

app.exec_()
