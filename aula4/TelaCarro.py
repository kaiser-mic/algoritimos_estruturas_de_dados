from telaVeiculo import TelaVeiculo
from PyQt5.QtWidgets import *
import sys
from Carro import Carro

class TelaCarro(TelaVeiculo):
    def __init__(self, titulo="tela do carro"):
        super().__init__(titulo)

    def definirlayout(self):
        super().definirlayout()
        self.lblportas = QLabel("Qtd Portas: ")
        self.txtportas = QLineEdit(self)
        self.layout.addWidget(self.lblportas)
        self.layout.addWidget(self.txtportas)


    def salvar(self):
        modelo = self.txtmodelo.text()
        if modelo != "":
            ano = self.txtano.text()
            valor = None
            if ano != "":
                valor = int(ano)

            portas = self.txtportas.text()
            vPortas = None
            if portas != "":
                vPortas = int(portas)
            carro = Carro(modelo, ano, vPortas)
            QMessageBox.information(self, "Carro Salvo", str(carro))
