import sys
from random import choice
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

titulos_janela = [  # 1
    'Meu App',
    'Meu App',
    'Ainda meu App',
    'Ainda meu App',
    'Mas que diabos',
    'Mas que diabos',
    'Isso é surpresa',
    'Isso é surpresa',
    'Algo deu errado'
]


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Meu App')

        self.botao = QPushButton('Me aperte!')
        self.botao.clicked.connect(self.botao_clicado)
        self.windowTitleChanged.connect(self.titulo_mudado)  # 2

        self.setCentralWidget(self.botao)

    def botao_clicado(self):
       print('Clicado')
       novo_titulo = choice(titulos_janela)
       print(f'Mudar o título para: {novo_titulo}')
       self.setWindowTitle(novo_titulo)  # 3

    def titulo_mudado(self, titulo_janela):
        print(f'O título mudou para: {titulo_janela}')  # 4
        if titulo_janela == 'Algo deu errado':
            self.botao.setDisabled(True)


app = QApplication(sys.argv)

janela = JanelaPrincipal()
janela.show()

app.exec_()
