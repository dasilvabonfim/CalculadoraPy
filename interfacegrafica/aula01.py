from PySide6.QtWidgets import QApplication, QPushButton,QWidget, QVBoxLayout,QHBoxLayout,QGridLayout,QMainWindow


def slot_example():
    print("jooj")
    
app = QApplication()
window = QMainWindow()


#layout
botao1 = QPushButton('Botão')
botao1.setStyleSheet('font-size: 40px; color:blue')

botao2 = QPushButton('Botão2')
botao2.setStyleSheet('Font-size: 80px; color:red')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('Font-size: 50px; color:black')

layout = QGridLayout()

layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)
##

#Widget
central_widget = QWidget()
central_widget.setLayout(layout)

#statusbar
status_bar = window.statusBar()
status_bar.showMessage('JOOJ')

#window
titulo = 'janela'
window.setCentralWidget(central_widget)
window.setWindowTitle(titulo)

#menu
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro Menu')
primeira_acao = primeiro_menu.addAction('JuuJ')
primeira_acao.triggered.connect(slot_example)

window.show()
app.exec()