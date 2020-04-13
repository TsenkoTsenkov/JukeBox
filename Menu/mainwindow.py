import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QGridLayout, QLabel
from PyQt5.QtGui import QFont 

credits = 0

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        
        self.text = "Credits: {0}".format(credits)
        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignBottom)

        mbtn = QPushButton('Music', self)
        mbtn.resize(mbtn.sizeHint())
        mbtn.move(120, 40)

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(120, 100)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('JukeBox')    
        self.show()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MainMenu()
    sys.exit(app.exec_())