import sys
from collections import defaultdict
import re
import random

class createDictionary():
	def __init__(self, argv):
		self.tweetFile = argv[1] #file with all tweets in format username \tab\ tweet
		self.pronFile = argv[2] # file with the pronunciation of dutch words
	
	def findLG(self, lglist):
		for n, lg in enumerate(reversed(re.findall(r'\[([^]]*)\]',lglist))):
			# loopen door elk karakter om hoofdletter te vinden plus karakter wat er op volgt
				for i,c in enumerate(reversed(lg)):
					if c.isupper():
						#return (lg[i:], n, len(re.findall(r'\[([^]]*)\]',lglist)))
						cha = len(lg) - (i +1)
						return (lg[cha:], n, 0)

						

		return False				
						

	def createPronDict(self):
		self.pronDict = defaultdict(list)
		for line in open(self.pronFile):
			elements = line.split("\\")
			if not self.findLG(elements[4]) == False:
				self.pronDict[elements[1]] = self.findLG(elements[4])
			
			'''laatste hoofdletter plus letters die volgen in lettergreep in laatste lettergreep. '''
			

			
	def createDic(self):
		self.resultDict = defaultdict(list)
		'''
		for i in range(50):
			string = input("woord: ")
			for key, value in self.pronDict.items():
				if self.pronDict[string][0] == self.pronDict[key][0] and self.pronDict[string][1] == self.pronDict[key][1] and self.pronDict[string][2] == self.pronDict[key][2]:
					print(key) 
		'''
		for line in open(self.tweetFile):
			elements = line.split('\t')
			lastWord = ''.join(elements[1].split()[-1:]	)
			if lastWord in self.pronDict:
				#print(tuple(self.pronDict[lastWord]))
				key = tuple(self.pronDict[lastWord])
				self.resultDict[key].append(elements[1].strip())
			
			'''
			if lastWord in self.pronDict:
				print(elements[1].strip())
				print(', '.join(self.findWords(self.pronDict[lastWord][0], self.pronDict[lastWord][1], self.pronDict[lastWord][2]) ))
			'''
		
		
		while 0 < 1:
			randomKey = random.choice(list(self.resultDict.keys()))
			if len(self.resultDict[randomKey]) > 1:
				tweet1 = random.choice(self.resultDict[randomKey])
				tweet2 = random.choice(self.resultDict[randomKey])
				
				print()
				print(tweet1)
				print(tweet2)
				print()
				inputUser = input('Press enter to continue, x to abort')
				if inputUser == 'x':
					break

		

	def findWords(self, lg, pos, length):
		result = []
		for key, value in self.pronDict.items():
				if lg == self.pronDict[key][0] and pos == self.pronDict[key][1] and length == self.pronDict[key][2]:
					result.append(key)  
		return result

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