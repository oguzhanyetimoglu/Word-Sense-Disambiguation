# edit deneme 
from bs4 import BeautifulSoup

with open("wordnet.xml") as wordnet:
	soup = BeautifulSoup(wordnet, "html.parser")

idToWordsDict = {}      # Dictionary: Key -> sysnet id,  Value -> List of words in that sysnet
# Hypernymler eklenecek
# Tanımlar eklenecek
wordToSensesDict = {}   # Dictionary: Key -> word, Value -> List of sense ids for that word


synsets = soup.find_all("synset")
for synset in synsets:
	synsetId = synset.id.string
	literals = synset.find_all("literal")
	words = []
	for literal in literals:
		# Buna başka bi çözüm bulmak lazım çünkü 'olmak<' diye token geliyo mesela
		# sense tagleri arasındaki sayı çift basamaklı olduğu zaman.
		word = str(literal)[9:-26]   
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

# Wordnete bunu hem yaz hem yazmak olarak sokmamız lazım çünkü wordnette yaz'ın fiil hali yok
# Burda zemberek falan kullanılacak
# Wordnette olmayan kelimeler için bi if kontrolü lazım yoksa program patlar

def calculate_scores(targetBags, bigBag):
	

def disambiguate(tokens, target):
	candidates = wordToSensesDict[target]
	candidates = candidates + wordToSensesDict[target + "mak"]
	#print(candidates)
	scoresDict = {}
	targetBags = []  # Target word'ümüzün tüm senselerinin bagleri
	bigBag = []      # Diğer her şeyin istiflendiği bag
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





	
