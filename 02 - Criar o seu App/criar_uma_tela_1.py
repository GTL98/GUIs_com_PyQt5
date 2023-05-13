from PyQt5.QtWidgets import QApplication, QWidget

# Necessário somente para acessar os argumetos da linha de comando.
import sys

# Você precisa de uma (e somente uma) instância do QApplication por aplicativo.
# Passe sys.argv para permitir argumentos de linha de comando para seu aplicativo.
# Se você sabe que não usará argumentos de linha de comando, QApplication([]) também funciona.
app = QApplication(sys.argv)

# Crie um widget Qt, que será a nossa tela
tela = QWidget()
tela.show()  # IMPORTANTE!!! As telas ficam ocultas por padrão

# Iniciar o loop de eventos
app.exec_()

# Seu aplicativo não chegará aqui até que saia e o evento tenha parado
