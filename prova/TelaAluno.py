import sys
from PyQt5.QtWidgets import *
from Aluno import Aluno

class TelaAluno(QMainWindow):
        def __init__(self, titulo = 'Tela Aluno', largura=300, altura=150):
            super().__init__()
            self.setWindowTitle(titulo)
            self.setGeometry(100, 100, largura, altura)
            self.layout = QVBoxLayout()
            self.definirlayout()

            self.buttonmatricular = QPushButton('matricular')
            self.buttonmatricular.clicked.connect(self.matricular)
            self.layout.addWidget(self.buttonmatricular)

            container = QWidget()
            container.setLayout(self.layout)
            self.setCentralWidget(container)
        
        def matricular(self):
              nome = self.txtnome.text()
              cpf = self.txtcpf.text()
              matricula = self.txtmatricula.text()

              aluno = Aluno(nome, cpf, matricula)
              QMessageBox.information(self, 'matricula', f'Aluno matriculado com sucesso com sucesso!\n{str(aluno)}')

              self.txtnome.clear()
              self.txtcpf.clear()
              self.txtmatricula.clear()

        def definirlayout(self):
              self.lblnome = QLabel("Nome: ")
              self.txtnome = QLineEdit(self)

              self.lblcpf = QLabel("cpf: ")
              self.txtcpf = QLineEdit(self)

              self.lblmatricula = QLabel("matricula: ")
              self.txtmatricula = QLineEdit(self)


              self.layout.addWidget(self.lblnome)
              self.layout.addWidget(self.txtnome)
              
              self.layout.addWidget(self.lblcpf)
              self.layout.addWidget(self.txtcpf)

              self.layout.addWidget(self.lblmatricula)
              self.layout.addWidget(self.txtmatricula)