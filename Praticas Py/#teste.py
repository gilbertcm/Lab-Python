from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
import sys

class MinhaJanela(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Minha Interface com PyQt")
        self.setGeometry(100, 100, 300, 200)

        self.label = QLabel("Olá, mundo!", self)
        self.botao = QPushButton("Clique Aqui", self)
        self.botao.clicked.connect(self.alterar_texto)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.botao)

        self.setLayout(layout)

    def alterar_texto(self):
        self.label.setText("Botão pressionado!")

# Criando e rodando a aplicação
app = QApplication(sys.argv)
janela = MinhaJanela()
janela.show()
sys.exit(app.exec_())
