import sys
from collections import defaultdict
import re

class createDictionary():
	def __init__(self, argv):
		self.tweetFile = argv[1] #file with all tweets in format username \tab\ tweet
		self.pronFile = argv[2] # file with the pronunciation of dutch words
	
	def createPronDict(self):
		self.pronDict = defaultdict(list)
		for line in open(self.pronFile):
			elements = line.split("\\")
			self.pronDict[elements[1]] = re.findall(r'\[([^]]*)\]',elements[4])

	def createDic(self):
		self.resultDict = defaultdict(list)
		for i in range(50):
			string = input("woord: ")
			print(self.pronDict[string])
		'''
		for line in open(self.tweetFile):
			elements = line.split('\t')
			key = self.createKey(elements[1])
			if not key == False and not key == None:
				self.resultDict[tuple(key)].append(elements)
		'''

	def createKey(self, tweet): #get the pronunciation of last two words of tweet
		words = tweet.split()	
		if len(words) > 3:
			words = words[-2:]	
			if words[0].lower().strip() in self.pronDic and words[1].lower().strip() in self.pronDic:
				return self.pronDic[words[0].lower().strip()], self.pronDic[words[1].lower().strip()]
			else: 
				return False

i = createDictionary(sys.argv)
i.createPronDict()
i.createDic()
#i.findTwieTweet()