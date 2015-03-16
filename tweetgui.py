#!usr/bin/python3.4

import sys
from PyQt4 import QtGui, QtCore
#from createDictionary import *
import random

class TweetGui(QtGui.QWidget):
	""" Docstring """

	def __init__(self, tweet1, tweet2):
		super(TweetGui, self).__init__()
		self.tweet1 = tweet1
		self.tweet2 = tweet2
		self.initUI()

	def initUI(self):
		self.grid = QtGui.QGridLayout()
		self.grid.setSpacing(5)
		self.tweetLabel = QtGui.QLabel()
		self.twietwietLabel = QtGui.QLabel()
		self.tweetButton = QtGui.QPushButton('Nieuwe tweet', self)
		self.twietwietButton = QtGui.QPushButton('Nieuwe twietwiet', self)

		self.tweetButton.setFixedWidth(150)
		self.twietwietButton.setFixedWidth(150)

		self.tweetButton.clicked.connect(self.buttonPushed)
		self.twietwietButton.clicked.connect(self.buttonPushed)

		self.grid.addWidget(self.tweetLabel, 1, 0)
		self.grid.addWidget(self.twietwietLabel, 2, 0)
		self.grid.addWidget(self.tweetButton, 1, 4)
		self.grid.addWidget(self.twietwietButton, 2, 4)

		self.setWindowIcon(QtGui.QIcon('icon.png'))
		self.setWindowTitle('TwieTwiet')
		self.setGeometry(500, 200, 400, 400)
		self.QMainWindow.setStyleSheet("background-image: url(background.jpg)")

		self.setLayout(self.grid)
		self.show()

	def buttonPushed(self):
		source = self.sender()

		if source.text() == "Nieuwe tweet":
			self.tweetLabel.setText(random.choice(self.tweet1))
		else:
			self.twietwietLabel.setText(random.choice(self.tweet2))


if __name__ == '__main__':
	tweet1 = ['haha', 'hoofd', 'osdopjfklasdjf', 'dkjfa;lskdfjads;', 'dkfjakjdk']
	tweet2 = ['kdjfkds', 'djkafjsd', 'kdsfajs;kdj', 'dsjfk;ajsd', 'djfkasdfjas;', 'djasfklasdjf']

	app = QtGui.QApplication(sys.argv)
	t = TweetGui(tweet1, tweet2)
	t.show()
	app.exec_()