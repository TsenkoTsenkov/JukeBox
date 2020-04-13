import sys
import pygame
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication)

sampleMusic = 'TortureDance.mp3'

class MusicMenu(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        jButton = QPushButton("Jazz")
        hButton = QPushButton("HipHop")
        rButton = QPushButton("Rock")

        jButton.clicked.connect(self.playMusic)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(jButton)
        hbox.addWidget(hButton)
        hbox.addWidget(rButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)    
        self.setGeometry(300, 300, 300, 150)
        self.show()
        
    def playMusic(self):

        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(sampleMusic)
        pygame.mixer.music.play()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MusicMenu()
    sys.exit(app.exec_())