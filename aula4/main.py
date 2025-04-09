import sys
from PyQt5.QtWidgets import QApplication
from telaVeiculo import TelaVeiculo
from TelaCarro import TelaCarro
app = QApplication(sys.argv)

telaVeiculo = TelaVeiculo("cadastro de veiculo")
telaVeiculo.show()

telacarro = TelaCarro("cadastro de carro")
telacarro.show()
sys.exit(app.exec_())