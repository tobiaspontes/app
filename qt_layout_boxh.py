# h_layout.py

"""Horizontal layout example."""

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QWidget,
)

app = QApplication([]) # instancia a classe QApplication que cria e gerencia a aplicação
window = QWidget() # instancia uma janela que conterá widgets
window.setWindowTitle("QHBoxLayout") # cria um título pra janela

layout = QHBoxLayout() # instancia a classe QHBoxLayout que coloca os widgets horizontalmente
layout.addWidget(QPushButton("Esquerda")) # acrescenta um botão com o texto 'Left'
layout.addWidget(QPushButton("Centro")) # acrescenta um botão com o texto 'Center'
layout.addWidget(QPushButton("Direita")) # acrescenta um botão com o texto 'Right'
window.setLayout(layout) # método setLayout define o layout da janela

window.show() # apresenta a janela para o usuário
sys.exit(app.exec()) # app.exec mantém o loop do app até que o usuário saia do aplicativo