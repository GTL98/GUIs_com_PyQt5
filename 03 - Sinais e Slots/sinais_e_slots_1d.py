import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.botao_esta_alterado = True

        self.setWindowTitle('Meu App')

        self.botao = QPushButton('Me aperte!')  # 1
        self.botao.setCheckable(True)
        self.botao.released.connect(self.botao_foi_liberado)  # 2
        self.botao.setChecked(self.botao_esta_alterado)

        self.setCentralWidget(self.botao)

    def botao_foi_liberado(self):
        self.botao_esta_alterado = self.botao.isChecked()  # 3
        print(self.botao_foi_liberado)


app = QApplication(sys.argv)

janela = JanelaPrincipal()
janela.show()

app.exec_()
