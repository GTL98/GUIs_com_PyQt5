import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Meu App')

        widget = QLabel('Olá')
        fonte = widget.font()  # 1
        fonte.setPointSize(30)
        widget.setFont(fonte)
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # 2

        self.setCentralWidget(widget)


app = QApplication(sys.argv)

janela = JanelaPrincipal()
janela.show()

app.exec_()
