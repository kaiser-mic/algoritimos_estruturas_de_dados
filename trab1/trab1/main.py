import sys
from PyQt5.QtWidgets import *
from TelaDesktop import TelaDesktop
from TelaNotebook import TelaNotebook

app = QApplication(sys.argv)
telaDesk = TelaDesktop()
telaDesk.show()
telaNote = TelaNotebook()
telaNote.show()
sys.exit(app.exec_())