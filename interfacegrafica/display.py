from PySide6.QtWidgets import QLineEdit,QMainWindow
from PySide6.QtCore import Qt
from variables import BIG_FONT_SIZE, MEDIUM_FONT_SIZE, SMALL_FONT_SIZE, DEFAULT_MARGIN,WIDTH

class Display(QLineEdit):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.configStyle()
        
    def configStyle(self):
        margem = [DEFAULT_MARGIN for _ in range (4)]
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignRight)
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(WIDTH)
        self.setTextMargins(*margem)