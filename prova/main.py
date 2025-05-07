import sys
from PyQt5.QtWidgets import *
from TelaAluno import TelaAluno

app = QApplication(sys.argv)
telaaluno = TelaAluno()
telaaluno.show()
sys.exit(app.exec_())