# dialog.py

"""Dialog-style application."""

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
)

class Window(QDialog):  # define a classe Window herdando a classe QDialog
    def __init__(self):
        super().__init__(parent=None) # chama o método __init__ da classe herdada; parent=None porque neste exemplo a caixa de diálogo será a janela principal
        self.setWindowTitle("QDialog")
        dialogLayout = QVBoxLayout() # instancia um layout vertical
        formLayout = QFormLayout() # instancia um layout de formulário
        formLayout.addRow("Nome:", QLineEdit()) # acrescenta linha ao formulário
        formLayout.addRow("Idade:", QLineEdit())
        formLayout.addRow("Trabalho:", QLineEdit())
        formLayout.addRow("Hobbies:", QLineEdit())
        dialogLayout.addLayout(formLayout) # embute o formulário no layout vertical
        buttons = QDialogButtonBox() # cria a caixa de botões inserida na caixa de diálogo
        buttons.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel
            | QDialogButtonBox.StandardButton.Ok
        ) # cria os botões "Cancel" e "Ok"
        dialogLayout.addWidget(buttons) # insere os botões na layout vertical
        self.setLayout(dialogLayout)

if __name__ == "__main__":
    app = QApplication([]) # instancia a classe QApplication que cria e gerencia a aplicação
    window = Window() # instancia a classe Window
    window.show() # apresenta a janela
    sys.exit(app.exec()) # cria loop de execução até que um evento termine a aplicação