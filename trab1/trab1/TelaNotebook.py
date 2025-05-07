import sys
from PyQt5.QtWidgets import *
from Notebook import Notebook

class TelaNotebook(QMainWindow):
    def __init__(self, titulo = 'Tela Notebook', largura=300, altura=150):
        super().__init__()
        self.setWindowTitle(titulo)
        self.setGeometry(100, 100, largura, altura)
        self.layout = QVBoxLayout()
        self.definirlayout()

        self.buttoncadastrar = QPushButton('cadastrar')
        self.buttoncadastrar.clicked.connect(self.cadastrar)
        self.layout.addWidget(self.buttoncadastrar)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    
    def cadastrar(self):
        modelo = self.txtmodelo.text()
        cor = self.txtcor.text()
        preco = self.txtpreco.text()
        categoria = self.txtcategoria.text()
        tempo = self.txttempo.text()

        notebook = Notebook(modelo, cor, preco, categoria, tempo)
        QMessageBox.information(self, 'Cadastro', f'Notebook cadastrado com sucesso!\n{notebook.getinformacoes()}')

        self.txtmodelo.clear()
        self.txtcor.clear()
        self.txtpreco.clear()
        self.txtcategoria.clear()
        self.txttempo.clear()




    def definirlayout(self):

        self.lblmodelo = QLabel('Modelo:')
        self.txtmodelo = QLineEdit(self)

        self.lblcor = QLabel('Cor:')
        self.txtcor = QLineEdit(self)
        
        self.lblpreco = QLabel('Preço:')
        self.txtpreco = QLineEdit(self)
        
        self.lblcategoria = QLabel('Categoria:')    
        self.txtcategoria = QLineEdit(self)
        
        self.lbltempo = QLabel('Tempo de Bateria:')
        self.txttempo = QLineEdit(self)


        self.layout.addWidget(self.lblmodelo)
        self.layout.addWidget(self.txtmodelo)
        
        self.layout.addWidget(self.lblcor)
        self.layout.addWidget(self.txtcor)
        
        self.layout.addWidget(self.lblpreco)
        self.layout.addWidget(self.txtpreco)
        
        self.layout.addWidget(self.lblcategoria)
        self.layout.addWidget(self.txtcategoria)
        
        self.layout.addWidget(self.lbltempo)
        self.layout.addWidget(self.txttempo)