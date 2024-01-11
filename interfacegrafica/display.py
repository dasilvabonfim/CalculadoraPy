from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from utils import isEmpty,isNumOrDot
from variables import BIG_FONT_SIZE, MEDIUM_FONT_SIZE, SMALL_FONT_SIZE, DEFAULT_MARGIN,WIDTH

class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)
    
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

    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return]
        isDelete = key in [KEYS.Key_Backspace, KEYS.Key_Delete]
        isEsc = key in [KEYS.Key_Escape]
        isOperator = key in [
            KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Slash, KEYS.Key_Asterisk,
            KEYS.Key_P,
        ]

        if isEnter:
            self.eqPressed.emit()
            return event.ignore()
        if isDelete:
            self.delPressed.emit()
            return event.ignore()

        if isEsc:
            self.clearPressed.emit()
            return event.ignore()
        if isOperator:
            if text.lower() == 'p':
                text = '^'
            self.operatorPressed.emit(text)
            return event.ignore()


        # Não passar daqui se não tiver texto
        if isEmpty(text):
            return event.ignore()

        if isNumOrDot(text):
            self.inputPressed.emit(text)
            return event.ignore()
            
            
            
            