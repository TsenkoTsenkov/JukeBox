import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QGridLayout, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QFont 
import pygame

'''
credits = 0
sampleMusic = 'TortureDance.mp3'

def playMusic(self):

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(sampleMusic)
    pygame.mixer.music.play()
'''

class MainWindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Main Window')

        layout = QtWidgets.QGridLayout()

        self.button = QtWidgets.QPushButton('Main')
        self.button.clicked.connect(self.switch)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def switch(self):
        self.switch_window.emit()


class MusicWindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Music')

        layout = QtWidgets.QGridLayout()

        self.button = QtWidgets.QPushButton('Music')
        self.button.clicked.connect(self.music)

        layout.addWidget(self.button)

        self.setLayout(layout)

    def music(self):
        self.switch_window.emit()


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


