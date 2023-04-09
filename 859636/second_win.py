# напиши здесь код для второго экрана приложения
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QListWidget, QLineEdit
from instr import *
from second_win import*

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
#__________________________________________________________________________________________________
    def initUI(self):
        self.hintname_text = QLabel(txt_hintname)
        self.line_name = QLineEdit("П.I.Б.")
        self.hintage = QLabel(txt_hintage)
        self.line_age = QLineEdit('0')
       
        # тест 1
        self.test1 = QLabel(txt_test1)
        self.btn_starttest1 = QPushButton(txt_starttest1)
       
        # тест 2
        self.test2 = QLabel(txt_test2)
        self.btn_starttest2 = QPushButton(txt_starttest2)

        # тест 3
        self.test3 = QLabel(txt_test3)
        self.btn_starttest3 = QPushButton(txt_starttest3)
        self.line_tst31 = QLineEdit('0')
        self.line_tst32 = QLineEdit('0')

        # Надіслати результати
        self.btn_sendresults = QPushButton(txt_sendresults)

        #Лейаути

        self.hor_line = QHBoxLayout()
        self.rig_line = QVBoxLayout()
        self.lef_line = QVBoxLayout()        

        self.hor_line.addLayout(self.lef_line)
        self.hor_line.addLayout(self.rig_line)
        self.setLayout(self.hor_line )

        self.lef_line.addWidget(self.hintname_text, alignment= Qt.AlignLeft)
        self.lef_line.addWidget(self.line_name, alignment= Qt.AlignLeft)
        self.lef_line.addWidget(self.hintage, alignment= Qt.AlignLeft)
        self.lef_line.addWidget(self.line_age, alignment= Qt.AlignLeft)
        self.lef_line.addWidget(self.test1, alignment= Qt.AlignLeft)
        self.lef_line.addWidget(self.btn_starttest1, alignment= Qt.AlignLeft)
        self.lef_line.addWidget(self.test2, alignment= Qt.AlignLeft)
        self.lef_line.addWidget(self.btn_starttest2, alignment= Qt.AlignLeft)
        self.lef_line.addWidget(self.test3, alignment= Qt.AlignLeft)
        self.lef_line.addWidget(self.btn_starttest3, alignment= Qt.AlignLeft)
        self.lef_line.addWidget(self.line_tst31, alignment= Qt.AlignLeft)
        self.lef_line.addWidget(self.line_tst32, alignment= Qt.AlignLeft)
        self.lef_line.addWidget(self.btn_sendresults, alignment= Qt.AlignCenter)

#__________________________________________________________________________________________________

    def next_click(self):
        self.fw = TestWin()
        self.hide()
    
    def connects(self):
        self.btn_sendresults.clicked.connect(self.next_click)

    def set_appear(self):
        self.setWindowTitle("Здоров'я")
        self.resize(win_width, win_height)
        self.move(win_x, win_y)

app = QApplication([])
tw = TestWin()
app.exec_()