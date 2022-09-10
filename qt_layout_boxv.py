# v_layout.py

"""Vertical layout example."""

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

app = QApplication([]) # instancia a classe QApllication que cria e gerencia a aplicação
window = QWidget() # instancia a classe QWidget que cria uma janela
window.setWindowTitle("QVBoxLayout") # define um título para a janela

layout = QVBoxLayout() # instancia a classe QVBoxLayout que cria um layout vertical
layout.addWidget(QPushButton("Topo")) # acrescenta um botão com o texto 'Top'
layout.addWidget(QPushButton("Centro")) # acrescenta um botão com o texto 'Center'
layout.addWidget(QPushButton("Rodapé")) # acrescenta um botão com o texto 'Bottom'
window.setLayout(layout) # define o layout da janela

window.show() # apresenta a janela
sys.exit(app.exec()) # cria um loop de execução até que ocorra um evento de saída