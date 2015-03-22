import sys
from collections import defaultdict
import re
import random

class twieTweets():
	def __init__(self):
		self.tweetFile = 'tweets.txt' #file with all tweets in format username \tab\ tweet
		self.pronFile = 'dpw.cd'# file with the pronunciation of dutch words
		self.createPronDict() # make dictionary of dpw.cd file
		self.createTwieTweets() #create dictionary of tweets that rhyme
	
	def syllables(self, syllables):
		'''[vu:d][bAl] Vind eerste hoofdletter vanaf rechts plus opvolgende karakters, eg Al'''
		''' als klemtoon in laatste lettergreep voorkomt dan is dat de regel waar we naar moeten zoeken
		als er geen klemtoon in de laatste lettergreep voorkomt en wel een : voorkomt en geen klemtoon daarna is 
		dat wat we moeten gebruiken'''
		#[hArd][lo:][p@]	
		lastPart = []	
		for n, syl in enumerate(reversed(re.findall(r'\[([^]]*)\]',syllables))):
				for i,c in enumerate(reversed(syl)):
					lastPart.append(c)
					if c == ':':
						return (syl[len(syl) - (i + 2):] + ''.join(reversed(lastPart))[1:], n)
					if c.isupper() and n == 0:		
						return (syl[len(syl) - (i +1):], n)
		return False										

	def createPronDict(self):
		'''Create dictionary with a tuple of syllable and position of syllable as key'''
		self.pronDict = defaultdict(list)
		self.syllablesList = defaultdict(list)
		for line in open(self.pronFile):
			elements = line.split("\\")
			if not self.syllables(elements[4]) == False:
				self.pronDict[elements[1]] = self.syllables(elements[4])
				self.syllablesList[elements[1]] = elements[4] #add all syllables for showing them after each tweet, test function

	def createTwieTweets(self):
		'''Maak een twieTweet dictionary op basis van laatste woord van tweet en bijbehorende klank. Resultaat is een 
		dictionary met als key de klank (hoofdletter plus opvolgende letters) en als values tweets die dat hebben'''
		self.twieTweets = defaultdict(list)
		for line in open(self.tweetFile, encoding='utf-8'):
			elements = line.split('\t')
			lastWord = self.getLastWord(elements[1])
			if lastWord in self.pronDict:
				key = tuple(self.pronDict[lastWord])
				self.twieTweets[key].append(elements[1].strip())
	
	def getLastWord(self, tweet):
		'''get last word of tweet (functie nog uitbreiden om hashtags etc te verwijderen via andere functie)'''
		lastWord = ''.join(tweet).split()[-1]

		i = -1
		while True:
			if len(lastWord) < 2:
				i = i - 1
				lastWord = ''.join(tweet).split()[i]
			elif '#' in lastWord and (len(''.join(tweet).split()) + i)>=1:
				i = i - 1
				lastWord = ''.join(tweet).split()[i]
			elif 'http' in lastWord and (len(''.join(tweet).split()) + i)>=1:
				i = i - 1
				lastWord = ''.join(tweet).split()[i]
			elif lastWord[-1] in str(list(range(10))):
				while lastWord[-1] in str(list(range(10))):
					lastWord = lastWord[:-1]
					if len(lastWord) < 2:
						i = i - 1
						lastWord = ''.join(tweet).split()[i]
			elif lastWord[-1] in ['.','?','!',',',':',')','(','@']:
				lastWord = lastWord[:-1]
				if len(lastWord) < 2:
					i = i - 1
					lastWord = ''.join(tweet).split()[i]
			else:
				break
		return lastWord

	def inputTweet(self):
		randomKey = random.choice(list(self.twieTweets.keys()))

		#testen hoeveel tweets eindigen op hetzelfde woord 
		while not len(self.twieTweets[randomKey]) > 2 :
			randomKey = random.choice(list(self.twieTweets.keys()))
		return random.choice(self.twieTweets[randomKey])
	
	def getTwieTweets(self):
		# get random list of tweets that rhyme
		result = defaultdict(list)
		while len(list(result.values())) < 2:
			result.clear()
			randomList = self.twieTweets[random.choice(list(self.twieTweets.keys()))]			
			for tweet in randomList:
				if self.getLastWord(tweet) in self.pronDict:
					result[self.getLastWord(tweet)] = tweet
		return list(result.values())
		

	def twieTweetTest(self):
		for tweet in self.getTwieTweets():
			print(tweet)
			

if __name__ == '__main__':
	twieTweets = twieTweets()
	twieTweets.twieTweetTest()

