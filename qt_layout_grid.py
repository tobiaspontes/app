# g_layout.py

"""Grid layout example."""

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QPushButton,
    QWidget,
)

app = QApplication([]) # instancia a classe QApplication que cria e gerencia a aplicação
window = QWidget() # instancia a classe QWidget que cria uma janela
window.setWindowTitle("QGridLayout") # define um título pra janela

layout = QGridLayout() # instancia a classe QGridLayout que cria um layout de grade
layout.addWidget(QPushButton("Botão (0, 0)"), 0, 0) # acrescenta um botão na linha 0 e coluna 0
layout.addWidget(QPushButton("Botão (0, 1)"), 0, 1) # acrescenta um botão na linha 0 e coluna 1
layout.addWidget(QPushButton("Botão (0, 2)"), 0, 2) # acrescenta um botão na linha 0 e coluna 2
layout.addWidget(QPushButton("Botão (1, 0)"), 1, 0) # acrescenta um botão na linha 1 e coluna 0
layout.addWidget(QPushButton("Botão (1, 1)"), 1, 1) # acrescenta um botão na linha 1 e coluna 1
layout.addWidget(QPushButton("Botão (1, 2)"), 1, 2) # acrescenta um botão na linha 1 e coluna 2
layout.addWidget(QPushButton("Botão (2, 0)"), 2, 0) # acrescenta um botão na linha 2 e coluna 0
layout.addWidget(
    QPushButton("Botão (2, 1) + 2 Colunas Expandidas"), 2, 1, 1, 2
) # argumentos de addWiget: widget, linha e coluna, expansão de linha e expansão de coluna
# acrescenta um botão na linha 2 e coluna 1, expandindo em 1 linha e 2 colunas
window.setLayout(layout) # define o layout da janela

window.show() # apresenta a janela
sys.exit(app.exec()) # cria loop de execução até que um evento termine a aplicação