import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QCheckBox, QMainWindow


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Meu App')

        widget = QCheckBox('Isso é uma checkbox')
        widget.setChecked(Qt.Checked)

        # Para um estado triplo: widget.setCheckState(Qt.PartiallyChecked)
        # Ou: widget.setTriState(True)
        widget.stateChanged.connect(self.mostrar_estado)

        self.setCentralWidget(widget)

    def mostrar_estado(self, estado):
        print(estado == Qt.Checked)
        print(estado)


app = QApplication(sys.argv)

janela = JanelaPrincipal()
janela.show()

app.exec_()
