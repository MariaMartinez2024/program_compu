import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class CalculadoraPromedio(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Promedio")
        self.setGeometry(100, 100, 400, 200)

        # Etiquetas y campos de texto
        self.label1 = QLabel("Ingrese la nota 1:")
        self.nota1 = QLineEdit()

        self.label2 = QLabel("Ingrese la nota 2:")
        self.nota2 = QLineEdit()

        self.label3 = QLabel("Ingrese la nota 3:")
        self.nota3 = QLineEdit()

        # Botones
        self.boton_calcular = QPushButton("Calcular")
        self.boton_limpiar = QPushButton("Limpiar")

        # Etiqueta para mostrar resultado
        self.resultado = QLabel("Promedio:")

        # Conectar botones a funciones
        self.boton_calcular.clicked.connect(self.calcular_promedio)
        self.boton_limpiar.clicked.connect(self.limpiar_campos)

        # Layouts
        layout = QVBoxLayout()

        layout.addWidget(self.label1)
        layout.addWidget(self.nota1)
        layout.addWidget(self.label2)
        layout.addWidget(self.nota2)
        layout.addWidget(self.label3)
        layout.addWidget(self.nota3)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.boton_calcular)
        h_layout.addWidget(self.boton_limpiar)

        layout.addLayout(h_layout)
        layout.addWidget(self.resultado)

        self.setLayout(layout)

    def calcular_promedio(self):
        try:
            n1 = float(self.nota1.text())
            n2 = float(self.nota2.text())
            n3 = float(self.nota3.text())
            promedio = (n1 + n2 + n3) / 3
            self.resultado.setText(f"Promedio: {promedio:.2f}")
        except ValueError:
            self.resultado.setText("Error: Ingrese solo números.")

    def limpiar_campos(self):
        self.nota1.clear()
        self.nota2.clear()
        self.nota3.clear()
        self.resultado.setText("Promedio:")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = CalculadoraPromedio()
    ventana.show()
    sys.exit(app.exec_())
