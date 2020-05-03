import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QStackedWidget, QApplication, QGridLayout, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QFont, QIcon, QPixmap
import pygame

credits = 0

class MainWindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Main Window')

        layout = QtWidgets.QGridLayout()

        self.button = QtWidgets.QPushButton('Music')
        self.button.clicked.connect(self.switch)
        layout.addWidget(self.button)

        self.button = QtWidgets.QPushButton('Quit')
        self.button.clicked.connect(QApplication.instance().quit)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.setGeometry(300, 300, 300, 300)

    def switch(self):
        self.switch_window.emit()

class MusicWindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Music')

        layout = QVBoxLayout()

        self.text = "Credits: {0}".format(credits)
        self.label = QLabel(self.text, self)
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        layout.addWidget(self.label)

        self.Stack = QStackedWidget()
        self.Stack.addWidget(MusicImageWidget('CanzoniPreferite.jpeg', "Canzoni Preferite", 'Daisuke Hasegawa'))

        layout.addWidget(self.Stack)

        self.button = QtWidgets.QPushButton('BackToMain')
        self.button.clicked.connect(self.music)
        layout.addWidget(self.button)

        layout.addStretch(1)

        self.setLayout(layout)
        self.setGeometry(300, 300, 800, 480)

    def music(self):
        self.switch_window.emit()

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

    def playMusic(self, songName):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(songName.replace(" ", "") + '.mp3')
        pygame.mixer.music.play()

class Controller:

    def __init__(self):
        self.music = MusicWindow()

    def show_music(self):
        self.window.close()
        self.music.switch_window.connect(self.show_main)
        self.music.show()

    def show_main(self):
        self.music.close()
        self.window = MainWindow()
        self.window.switch_window.connect(self.show_music)
        self.window.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_main()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


