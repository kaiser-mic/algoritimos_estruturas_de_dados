import sys
from PyQt5.QtWidgets import *
from Categoria import Categoria
from TelaCarro import TelaCarro

class TelaCategoria( QMainWindow ):
    def __init__(self, titulo = "tela de categoria", categorias = [], telaCar = None):
        self.telaCarro = telaCar
        super().__init__()
        self.categorias  =categorias
        self.setWindowTitle(titulo)
        self.setGeometry(500, 150, 150, 150)
        self.layout = QVBoxLayout()
        self.definirLayout()

        self.btnSalvar = QPushButton("salvar", self)
        self.btnSalvar.clicked.connect(self.salvar)
        self.layout.addWidget(self.btnSalvar)
        
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
    def salvar(self):
        nome = self.txtnome.text()
        if nome != "":
            cat = Categoria(nome)
            self.categorias.append(cat)
            QMessageBox.information(self, "Categoria salva", str(cat))
            if self.telaCarro is not None:
                self.telaCarro.carregarCategorias()
            self.txtnome.setText("")
            self.hide()

    def definirLayout(self):
        self.lblnome = QLabel("nome: ")
        self.txtnome = QLineEdit(self)

        self.layout.addWidget( self.lblnome)
        self.layout.addWidget( self.txtnome)