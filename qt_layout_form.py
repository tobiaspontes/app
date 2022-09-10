# f_layout.py

"""Form layout example."""

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QFormLayout,
    QLineEdit,
    QWidget,
)

app = QApplication([]) # instancia a classe QApplication que cria e gerencia a aplicação
window = QWidget() # instancia a classe QWidget que cria uma janela
window.setWindowTitle("QFormLayout") # define um título pra janela

layout = QFormLayout() # instancia a classe QFormLayout que cria um layout de formulário
layout.addRow("Nome:", QLineEdit()) # acrescenta linha ao formulário com label e campo de entrada
layout.addRow("Idade:", QLineEdit()) # acrescenta linha ao formulário com label e campo de entrada
layout.addRow("Trabalho:", QLineEdit()) # acrescenta linha ao formulário com label e campo de entrada
layout.addRow("Hobbies:", QLineEdit()) # acrescenta linha ao formulário com label e campo de entrada
window.setLayout(layout) # define o layout da janela

window.show() # apresenta a janela
sys.exit(app.exec()) # cria loop de execução até que um evento termine a aplicação