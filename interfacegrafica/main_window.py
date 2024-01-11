from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QMessageBox
import qdarkstyle

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget| None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)
            
        self.setWindowTitle('Calculadora')
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())





        self.setFixedSize(600,500)
            

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
    
    def addWidgetToVLayout(self, widget: QWidget):
        self.v_layout.addWidget(widget)
    
    def makeMsgBox(self):
        return QMessageBox(self)