from PyQt5.QtWidgets import QApplication, QPushButton
import sys

app = QApplication(sys.argv)

tela = QPushButton('Me aperte')
tela.show()

app.exec_()
