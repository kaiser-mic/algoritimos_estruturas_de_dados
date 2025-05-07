import sys
from PyQt5.QtWidgets import *
from Veiculo import Veiculo


class TelaVeiculo( QMainWindow ):
    def __init__(self, titulo = "tela de veiculo",):
        super().__init__()
        self.setWindowTitle(titulo)
        self.setGeometry(100, 150, 300, 150)
        self.layout = QVBoxLayout()
        self.definirLayout()

        self.btnSalvar = QPushButton("salvar", self)
        self.btnSalvar.clicked.connect(self.salvar)
        self.layout.addWidget(self.btnSalvar)
        
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
    def salvar(self):
        modelo = self.txtmodelo.text()
        if modelo != "":
            ano = self.txtano.text()
            valor = None
            if ano != "":
                valor = int(ano)

            veiculo = Veiculo(modelo, valor)
            QMessageBox.information(self, "Veiculo Salvo", str(veiculo))


    def definirLayout(self):
        self.lblmodelo = QLabel("Modelo: ")
        self.txtmodelo = QLineEdit(self)
        self.lblano = QLabel("Ano: ")
        self.txtano = QLineEdit(self)

        self.layout.addWidget( self.lblmodelo)
        self.layout.addWidget( self.txtmodelo)
        self.layout.addWidget( self.lblano)
        self.layout.addWidget( self.txtano)