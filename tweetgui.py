#!usr/bin/python3.4

import sys
from PyQt4 import QtGui, QtCore
import twieTweets
import random

class TweetGui(QtGui.QWidget):
	""" Docstring """

	def __init__(self):
		super(TweetGui, self).__init__()
		self.initUI()

	def initUI(self):
		self.bg = QtGui.QFrame(self)
		self.resolution = QtGui.QDesktopWidget().screenGeometry()
		self.bg.resize(self.resolution.width(),self.resolution.height())
		self.bg.setStyleSheet('background-image: url("background.jpg")')

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
		self.center()
		self.setWindowTitle('TwieTwiet')
		self.setGeometry(500, 200, 400, 400)
		#self.QMainWindow.setStyleSheet("background-image: url(background.jpg)")

		self.setLayout(self.grid)
		self.show()

	def buttonPushed(self):
		source = self.sender() 
		i = 0 #kan gebruikt worden om te loopen in mogelijke twietweets
		if source.text() == "Nieuwe tweet":
			self.tweets = self.getTweets()
			self.tweetLabel.setText(self.tweets[0])
			self.twietwietLabel.setText(self.tweets[1][i])
		else:
			self.twietwietLabel.setText(self.tweets[1][i]) #laat nu alleen eerste zien maar in deze list zitten meer tweets die hier op rijmen

	def getTweets(self):
		tweets = twieTwiet.getTwieTweets() #returns a list of tweets
		firstTweet = tweets.pop() #moet eigenlijk random gebeuren
		result = [firstTweet, tweets]
		return result

	def center(self):
		""" Centers the window of the application on the screen."""
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())


if __name__ == '__main__':	
	twieTwiet = twieTweets.twieTweets()
	app = QtGui.QApplication(sys.argv)
	t = TweetGui()
	t.show()
	app.exec_()