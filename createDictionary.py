import sys
from collections import defaultdict
import re
import random

class createDictionary():
	def __init__(self, argv):
		self.tweetFile = argv[1] #file with all tweets in format username \tab\ tweet
		self.pronFile = argv[2] # file with the pronunciation of dutch words
		self.createPronDict() # make dictionary of dpw.cd file
		self.createTwieTweets() #create dictionary of tweets that rhyme
	
	def syllables(self, syllables):
		'''[vu:d][bAl] Vind eerste hoofdletter vanaf rechts plus opvolgende karakters, eg Al'''
		for n, syl in enumerate(reversed(re.findall(r'\[([^]]*)\]',syllables))):
				for i,c in enumerate(reversed(syl)):
					if c.isupper():		
						return (syl[len(syl) - (i +1):], n)
		return False										

	def createPronDict(self):
		'''Create dictionary with a tuple of syllable and position of syllable as key'''
		self.pronDict = defaultdict(list)
		for line in open(self.pronFile):
			elements = line.split("\\")
			if not self.syllables(elements[4]) == False:
				self.pronDict[elements[1]] = self.syllables(elements[4])
	
	def createTwieTweets(self):
		'''Maak een twieTweet dictionary op basis van laatste woord van tweet en bijbehorende klank. Resultaat is een 
		dictionary met als key de klank (hoofdletter plus opvolgende letters) en als values tweets die dat hebben'''
		self.twieTweets = defaultdict(list)
		for line in open(self.tweetFile):
			elements = line.split('\t')
			lastWord = ''.join(elements[1].split()[-1:]	)
			if lastWord in self.pronDict:
				key = tuple(self.pronDict[lastWord])
				self.twieTweets[key].append(elements[1].strip())
	
	def twieTweet(self):
		while 0 < 1:
			randomKey = random.choice(list(self.twieTweets.keys()))
			if len(self.twieTweets[randomKey]) > 1:
				tweet1 = random.choice(self.twieTweets[randomKey])
				tweet2 = random.choice(self.twieTweets[randomKey])
				print()
				print(tweet1)
				print(tweet2)
				print()
				inputUser = input('Press enter to continue, x to abort')
				if inputUser == 'x':
					break
	

twieTweets = createDictionary(sys.argv)
twieTweets.twieTweet()

