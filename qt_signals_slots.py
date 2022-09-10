# signals_slots.py

"""Signals and slots example."""

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from functools import partial # utilizado para passar parâmetro no signal do widget

def saudar(nome):
    if msgLabel.text():
        msgLabel.setText('') # limpa o texto do label
    else:
        msgLabel.setText(f'Alô, {nome}!') # apresenta o texto do label

app = QApplication([]) # instancia a aplicação
window = QWidget() # instancia uma janela
window.setWindowTitle("Signals and slots") # dá um título pra janela
layout = QVBoxLayout() # instancia um layout vertical onde serão inseridos os widgets

button = QPushButton("Saudação") # instancia um botão com o texto 'Saudação'
button.clicked.connect(partial(saudar, 'Tobias')) # signal = clicked, conecta com o slot 'saudar' e passa o parâmetro 'Tobias'

layout.addWidget(button) # acrescenta o botão ao objeto layout
msgLabel = QLabel("") # instancia um label sem texto
layout.addWidget(msgLabel) # acrescenta o label ao layout
window.setLayout(layout) # define o layout da janela
window.show() # apresenta a janela
sys.exit(app.exec()) # cria loop de execução até que um evento termine a aplicação