from bs4 import BeautifulSoup

with open("wordnet.xml") as wordnet:
	soup = BeautifulSoup(wordnet, "html.parser")

idToWordsDict = {}   # synset id'si ile o id'ye ait kelimeler listesi
# Hypernymler eklenecek
# Tanımlar eklenecek
wordToSensesDict = {}


synsets = soup.find_all("synset")
for synset in synsets:
	synsetId = synset.id.string
	literals = synset.find_all("literal")
	words = []
	for literal in literals:
		word = str(literal)[9:-26]   # Buna başka bi çözüm bulmak lazım çünkü olmak< falan geliyo
		words.append(word)
		if word not in wordToSensesDict:
			wordToSensesDict[word] = [synsetId]
		else:
			wordToSensesDict[word].append(synsetId)
	#print(str(words))
	idToWordsDict[synsetId] = words

#print(str(idToWordsDict))
#print(str(wordToSensesDict))

sentence = "yaz gelmek bahar kış"

tokens = sentence.split()
target = "yaz"  
# Wordnete bunu hem yaz hem yazmak olarak sokmamız lazım
# Burda zemberek falan şart
# Olmayan kelimeler için kontrol şart

def calculate_scores(targetBags, bigBag):
	

def disambiguate(tokens, target):
	candidates = wordToSensesDict[target]
	candidates = candidates + wordToSensesDict[target + "mak"]
	#print(candidates)
	scoresDict = {}
	targetBags = []
	bigBag = []
	for senseId in candidates:
		bag = []
		synset = idToWordsDict[senseId]
		for word in synset:
			bag.append(word)
		targetBags.append(bag)

	for token in tokens:
		if token != target:
			senses = wordToSensesDict[token]
			for senseId in senses:
				words = idToWordsDict[senseId]
				for word in words:
					bigBag.append(word)


	print(bigBag)
	print(targetBags)
	scores = calculate_scores(targetBags, bigBag)





disambiguate(tokens, target)





	