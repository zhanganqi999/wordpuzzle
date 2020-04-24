import random
import queue


# cleanWords():Try to remove all illegal words from the words list
# input: words: the words list . 
# output: The list of words which are ok for use.
def cleanWords(words):
	newwords=set()
	for word in words:
		word = word.replace("\n","")
		test_write=word
		test_write=test_write.replace(" ","")
		test_write=test_write.replace(".","")
		test_write=test_write.replace("/","")
		test_write=test_write.replace("(","")
		test_write=test_write.replace("!","")
		if test_write==word:
			newwords.add(word)
	return(list(newwords))
# getWords(): Try to get a number of words randomly defined by "number"
# input: words/words list, number/the number to words to get
# output: the list of the words with the count is "number"
def getWords(words,number):
	validwordsidx=set()
	validWords = []
	linecount=len(words)
	while(len(validwordsidx)<number):
		r = random.randint(0,linecount-1)
		validwordsidx.add(r)
	for line in validwordsidx:
		validWords.append(words[line])
	return(validWords)
def checkPuzzle(links,status):
	q =queue.Queue()
	q.put(0)
	while(not q.empty()):
		idx=q.get()
		if(status[idx]==1):
			continue
		else:
			if(len(links[idx])>0):
				status[idx]=1
				while(len(links[idx])>0):
					q.put(links[idx].pop())
	isOK=True
	for n in range(len(status)):
		if(status[n]!=1):
			isOK=False
			break
	return(isOK)

# calculate(): Try to create data structure(DS) for the puzzle words
# input: validwords/to be puzzled.
# output:
def calculate(validwords):
	ln = len(validwords)
	#Try to init the DS
	repeatLetters = [set() for i in range(ln)]
	links =[set() for i in range(ln)]
	status = [0 for i in range(ln)]
	#Try to fill data into DS.
	for w in range(ln-1):
		for n in validwords[w]:
			xy=w+1
			while(xy<ln):
				if n in validwords[xy]:
					repeatLetters[w].add(n)
					repeatLetters[xy].add(n)
					links[w].add(xy)
					links[xy].add(w)
				xy+=1
	# print("words:",validwords)
	# print("repeatLetters:",repeatLetters)
	# print("links:",links)
	# print("status:",status)
	return(repeatLetters,links,status)


def main():
	coverletters="=*$#%&~+"
	isOK = False
	file=open("ket.txt","r")
	alllines=file.readlines()
	file.close()
	newlines = cleanWords(alllines)

	linecount=len(newlines)
	valid_words = getWords(newlines,3)
	for word in valid_words:
		newlines.remove(word)
	rls,lnks,sts=calculate(valid_words)
	isOK = checkPuzzle(lnks,sts)
	wordcount=3
	while(not isOK and wordcount<10):
		newwords=getWords(newlines,1)
		valid_words.append(newwords[0])
		wordcount+=1
		for word in newwords:
			newlines.remove(word)
		rls,lnks,sts=calculate(valid_words)
		isOK = checkPuzzle(lnks,sts)
		print("zg.debug:",wordcount)
		
	if(not isOK):
		print("wordcount:",wordcount)
	#print("valid_words:",valid_words)
	#print(rls,lnks,sts)
	alllettters=set()
	for idx in range(len(rls)):
		alllettters=alllettters.union(rls[idx])
	alllettters=list(alllettters)
	print(len(alllettters))
	for word in valid_words:
		for idx in range(len(alllettters)):
			word=word.replace(alllettters[idx],coverletters[idx])
		print(word)
	ans=input("")
	print(valid_words)

if __name__== "__main__":
	main()