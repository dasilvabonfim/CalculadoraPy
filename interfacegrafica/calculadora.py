import sys
from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOW_ICON_PATH
from buttons import Button,ButtonGrid

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addWidgetToVLayout(info)
    # Tela
    display = Display()
    window.addWidgetToVLayout(display)
    #grid
    buttonGrid = ButtonGrid(display)
    window.v_layout.addLayout(buttonGrid)
    
    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()