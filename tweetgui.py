#!usr/bin/python3.4

import sys
from PyQt4 import QtGui, QtCore, uic
import twieTweets
import random
import time


class FavTweets(QtGui.QDialog):
	'''Popup met tweets waarin het keyword voorkomt'''
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self)
		self.setGeometry(400, 250, 300, 500)
		self.setWindowTitle('Fav tweets')
		uic.loadUi('showFav.ui', self) 
		self.loadTweets()
	
	def loadTweets(self):
		entries = []
		for tweet in open('favTweets.txt'):
			entries.append(tweet.strip().split("\t"))
		self.table.setRowCount(len(entries))
		self.table.setColumnCount(2)
		for i, row in enumerate(entries):  	
			self.table.setItem(i, 0, QtGui.QTableWidgetItem(row[0]))
			self.table.setItem(i, 1, QtGui.QTableWidgetItem(row[1]))

class TweetGui(QtGui.QWidget):
	""" Docstring """

	def __init__(self):
		super(TweetGui, self).__init__()
		self.initUI()
		self.showMoreInfo = False #default setting
		

	def initUI(self):
		self.bg = QtGui.QFrame(self)
		self.resolution = QtGui.QDesktopWidget().screenGeometry()
		self.bg.resize(self.resolution.width(),self.resolution.height())
		self.bg.setStyleSheet('background-image: url("background.jpg")')

		self.grid = QtGui.QGridLayout()
		self.grid.setSpacing(5)
		
		self.tweetshow = QtGui.QPushButton('', self)
		self.twietwietshow = QtGui.QPushButton('', self)
		self.tweetButton = QtGui.QPushButton('Nieuwe tweet', self)
		self.twietwietButton = QtGui.QPushButton('Nieuwe twietwiet', self)
		self.tweetSaveButton = QtGui.QPushButton('Bewaar', self)
		self.tweetCopyButton = QtGui.QPushButton('Favorieten bekijken', self)
		self.bestTweetList=QtGui.QListWidget()
		self.clipBoard = QtGui.QApplication.clipboard()

		self.tweetshow.setToolTip('Klik om originele tweet te zien')
		self.twietwietshow.setToolTip('Klik om originele tweet te zien')

		self.tweetshow.setStyleSheet('background-color: rgba(255, 255, 255, 10); text-align: left')
		self.twietwietshow.setStyleSheet('background-color: rgba(255, 255, 255, 10); text-align: left')
		self.bestTweetList.setStyleSheet('background-color: rgba(255, 255, 255, 10); text-align: left')
		
		self.tweetButton.setFixedWidth(150)
		self.twietwietButton.setFixedWidth(150)
		self.tweetSaveButton.setFixedWidth(150)
		self.tweetCopyButton.setFixedWidth(150)
		

		self.tweetshow.clicked.connect(self.showMoreInfo)
		self.twietwietshow.clicked.connect(self.showMoreInfo)
		self.tweetButton.clicked.connect(self.buttonPushed)
		self.twietwietButton.clicked.connect(self.buttonPushed)
		self.tweetCopyButton.clicked.connect(self.showFavorites)
		self.tweetSaveButton.clicked.connect(self.saveTweet)

		self.grid.addWidget(self.tweetshow, 1, 0, 1, 3)
		self.grid.addWidget(self.twietwietshow, 2, 0, 1, 3)
		self.grid.addWidget(self.tweetButton, 1, 4)
		self.grid.addWidget(self.twietwietButton, 2, 4)
		self.grid.addWidget(self.tweetCopyButton, 3, 0, 1, 1)
		self.grid.addWidget(self.tweetSaveButton, 3, 1, 1, 1)

		self.setWindowIcon(QtGui.QIcon('icon.png'))
		self.setWindowTitle('TwieTwiet')
		self.setFixedSize(self.resolution.width()-(self.resolution.width()/4), 300)
		self.center()

		self.setLayout(self.grid)
		self.show()

	def popupBox(self, message):
		source = self.sender()
		self.messageBox = QtGui.QMessageBox.information(self, 'Bericht', message, QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
		
	def showMoreInfo(self):
		if self.showMoreInfo == True:
			self.showMoreInfo = False
			self.tweetshow.setText(self.tweets[0][1])
			self.twietwietshow.setText(self.tweets[1][0][1])
		else:
			self.showMoreInfo = True
			self.tweetshow.setText(self.tweets[0][0])
			self.twietwietshow.setText(self.tweets[1][0][0])

	def buttonPushed(self):
		source = self.sender() 
		if source.text() == "Nieuwe tweet":
			self.tweets = self.getTweets()
			self.tweetshow.setText(self.tweets[0][0])
			self.twietwietshow.setText(self.tweets[1][0][0])
		else:
			if len(self.tweets[1]) > 1:
				self.twietwietshow.setText(self.tweets[1][1][0])
				self.tweets[1].pop(0)
			else:
				self.popupBox("Helaas, Twietwiets zijn op!")

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

	def saveTweet(self):
		f = open('favTweets.txt', 'a')
		f.write("{} \t {}\n".format(self.twietwietshow.text(), self.tweetshow.text()))
		f.close()

	def copyTweet(self):
		self.bestTweet=[self.tweetshow.text() + '->' + self.twietwietshow.text()]
		self.bestTweetList.addItems(self.bestTweet)
		self.bestTweetList.setFixedSize(self.bestTweetList.sizeHintForColumn(0) + 2 * self.bestTweetList.frameWidth(), self.bestTweetList.sizeHintForRow(0) * self.bestTweetList.count() + 2 * self.bestTweetList.frameWidth())
		self.grid.addWidget(self.bestTweetList, 6, 0)
		self.clipBoard.setText(' '.join(self.bestTweet), mode=self.clipBoard.Clipboard)

	def showFavorites(self):
		self.dialog = FavTweets()
		self.dialog.show()



if __name__ == '__main__':	
	
	app = QtGui.QApplication(sys.argv)
	splash_pix = QtGui.QPixmap('background_splash.jpg')
	splash = QtGui.QSplashScreen(splash_pix)
	splash.show()
	# Tekstgrootte? en center !=center, verspringt bij laden.
	splash.showMessage("Welkom in Pretweetweet, het programma om rijm mee op te sporen!",alignment = QtCore.Qt.AlignCenter)
	twieTwiet = twieTweets.twieTweets()
	t = TweetGui()
	t.show()
	splash.finish(t)
	app.exec_()
	