import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QDialog, QMessageBox, QStackedWidget, QScrollArea, QGroupBox, QFormLayout, QApplication, QGridLayout, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import QTimer
import pygame

credits = 1

class MusicWindow(QtWidgets.QWidget):

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Music')

        groupBox = QGroupBox()
        layout = QHBoxLayout()

        layout.addWidget(MusicImageWidget('CanzoniPreferite.jpeg', "Canzoni Preferite", 'Daisuke Hasegawa'))
        layout.addWidget(MusicImageWidget('FightingGold.png', 'Fighting Gold', 'Coda'))
        layout.addWidget(MusicImageWidget('CanzoniPreferite.jpeg', "Canzoni Preferite", 'Daisuke Hasegawa'))
        layout.addWidget(MusicImageWidget('CanzoniPreferite.jpeg', "Canzoni Preferite", 'Daisuke Hasegawa'))
        layout.addWidget(MusicImageWidget('CanzoniPreferite.jpeg', "Canzoni Preferite", 'Daisuke Hasegawa'))
        layout.addStretch(1)

        groupBox.setLayout(layout)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(230)

        lay = QVBoxLayout(self)
        lay.addWidget(scroll)

        self.button = QtWidgets.QPushButton('Quit')
        self.button.clicked.connect(QApplication.instance().quit)
        lay.addWidget(self.button)
        
        self.setLayout(lay)
        self.setGeometry(0, 2, 800, 480)
        self.show()

class MusicImageWidget(QWidget):

    def __init__(self, icon, songName, artistName, parent=None):
        self.icon = icon
        self.songName = songName
        self.artistName = artistName

        QWidget.__init__(self, parent=parent)
        
        lay = QVBoxLayout(self)
        self.button = QPushButton()
        self.button.setIcon(QIcon(QPixmap(icon)))
        self.button.setIconSize(QtCore.QSize(100, 100))
        self.button.clicked.connect(lambda : self.playMusic(self.songName))
        
        lay.addWidget(self.button)

        self.text = "{0}".format(self.songName)
        self.label = QLabel(self.text, self)
        self.label.setFont(QFont("Helvetica", 12, QFont.Bold))
        lay.addWidget(self.label)

        self.text = "{0}".format(self.artistName)
        self.label = QLabel(self.text, self)
        self.label.setFont(QFont("Helvetica", 10))
        lay.addWidget(self.label)

        lay.addStretch(1)

    def playMusic(self, songName):
        global credits
        if pygame.mixer.get_busy():
            QMessageBox.about(self, "Error", "You have to wait for your song")

        elif credits > 0:
            pygame.mixer.music.load(songName.replace(" ", "") + '.mp3')
            pygame.mixer.music.play()
            credits = credits - 1
        else:
            QMessageBox.about(self, "Error", "Insert a token")

def main():
    app = QtWidgets.QApplication(sys.argv)
    jukeBox = MusicWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


