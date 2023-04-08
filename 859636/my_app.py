# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit
from instr import *
from second_win import*

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def initUI(self):
        self.btn_next= QPushButton(txt_next)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)

        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment= Qt.AlingLeft)
        self.layout_line.addWidget(self.instruction, alignment= Qt.AlingLeft)
        self.layout_line.addWidget(self.btn_next, alignment= Qt.AlingCenter)
        self.setLayout(self.layout_line)

    def next_click(self):
        self.tw = TestWin()
        self.hide()
    
    def connects(self):
        self.btn_next.clicled.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

app = QApplication([])

mw=MainWin()

app.exec_() 