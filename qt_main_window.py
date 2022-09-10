# main_window.py

"""Main window-style application."""

import sys

from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QStatusBar,
    QToolBar,
)

class Window(QMainWindow): # cria classe herdando de QMainWindow
    def __init__(self):
        super().__init__(parent=None) # inicializa como a classe herdada
        self.setWindowTitle("QMainWindow") # título
        self.setCentralWidget(QLabel("Eu sou o Widget Central")) # widget central 
        self._createMenu() # chama função para criar menu
        self._createToolBar() # chama função para criar uma barra de ferramentas
        self._createStatusBar() # chama função para criar uma barra de status

    def _createMenu(self):   # função para criar o menu
        menu = self.menuBar().addMenu("&Menu") # instancia classe menuBar e cria menu
        menu.addAction("&Exit", self.close) # adiciona um comando para sair do app

    def _createToolBar(self): # função para criar a barra de ferramentas
        tools = QToolBar() # instancia classe QToolBar
        tools.addAction("Exit", self.close) # adiciona uma ferramenta para sair do app
        self.addToolBar(tools) # cria barra de ferramentas

    def _createStatusBar(self): # função para criar barra de status
        status = QStatusBar() # instancia a classe QStatusBar
        status.showMessage("Eu sou a Barra de Status") # mensagem da barra de status
        self.setStatusBar(status) # cria a barra de status

if __name__ == "__main__":
    app = QApplication([])  # instancia a classe QApplication; classe que controla o fluxo do app
    window = Window() # instancia a classe Window
    window.show() # mostra a janela
    sys.exit(app.exec()) # executa o app em loop até que o usuário saia