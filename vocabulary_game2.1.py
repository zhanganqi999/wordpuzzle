import random
import queue
DEBUG=False
def zprint(*args):
	if(DEBUG):
		print("zg.debug:",args)
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
# checkPuzzle():Check whether all words are connected
# input: links/status , to list of data caculated.
# output: ok or not
def checkPuzzle(links):
	linkscpy=copyArrayOfSets(links)
	q =queue.Queue()
	q.put(0)
	status = [0 for i in range(len(linkscpy))]
	while(not q.empty()):
		idx=q.get()
		# print("zg debug:checkPuzzle:idx,status:",idx,status)
		if(status[idx]==1):
			continue
		else:
			if(len(linkscpy[idx])>0):
				status[idx]=1
				while(len(linkscpy[idx])>0):
					q.put(linkscpy[idx].pop())
	isOK=isDone(status)
	return(isOK)
# Try to copy the array of sets.
def copyArrayOfSets(arrayofsets):
	#Copy the list firstly. 
	#REMEMBER: All sets in it are still reference the old ones.
	arrayofsetscpy = arrayofsets.copy()
	for x in range(len(arrayofsets)):
		arrayofsetscpy[x]=arrayofsets[x].copy()
	return arrayofsetscpy

def isDone(status):
	isDone=True
	for n in range(len(status)):
		if(status[n]!=1):
			isDone=False
			break
	return(isDone)	
#findPath: try to find a path 
def findPath(links,rls):
	repeatlts = copyArrayOfSets(rls)
	linkscpy = copyArrayOfSets(links)
	zprint("findPath:links,rls",links,rls)
	path=[]
	linkrls = []
	#Let's start from 0
	#Let's try to find the shortest rls.
	biglen = 99
	idx=0
	for x in range(len(repeatlts)):
		if(len(repeatlts[x])<biglen):
			idx=x
			biglen=len(repeatlts[x])

	linkrls.append(idx)
	wordslen = len(repeatlts)
	found=True
	# print("in findPath:",repeatlts,linkscpy)
	while(len(linkrls)<wordslen and found):
		# If not found through following loop, that means the words are not linked.
		found=False
		#try to find the next node.
		i = len(linkrls)-1
		while(not found and i>-1):
			x =linkrls[i]
			#zprint("in findPath:x",x)
			if(len(linkscpy[x])>0):
				while(len(linkscpy[x])>0):
					nn = linkscpy[x].pop()
					samelts = repeatlts[x]&repeatlts[nn]
					if(len(samelts)>0):
						onelt = set(samelts.pop())
						repeatlts[x] = repeatlts[x]-onelt
						repeatlts[nn] = repeatlts[nn]-onelt
						linkrls.append(nn)
						linkscpy[nn].remove(x)
						path.append((x,onelt,nn))
						zprint("in findPath:path:",path)
						zprint("in findPath:linkrls,repeatlts:",linkrls,repeatlts)
						found=True
						break
					else:
						zprint("findPath:ERROR,x,nn:",x,nn)
						zprint("findPath:ERROR,linkrls,repeatlts:",linkrls,repeatlts)
			i-=1
	#print("in findPath:path:",path)
	if(found and i>-1):
		return(path)
	else:
		return([])

# calculate(): Try to create data structure(DS) for the puzzle words
# input: validwords/to be puzzled.
# output:
def calculate(validwords):
	ln = len(validwords)
	#Try to init the DS
	repeatLetters = [set() for i in range(ln)]
	links =[set() for i in range(ln)]
	
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

	return(repeatLetters,links)


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
	#For test:
	# valid_words=['closed', 'autumn', 'physics']
	# valid_words=['bee', 'toast', 'red', 'low', 'aeroplane']
	rls,lnks=calculate(valid_words)
	
	isOK = checkPuzzle(lnks)
	# zprint("in main:isOK:",isOK)
	wordcount=len(valid_words)
	while(not isOK and wordcount<10):
		newwords=getWords(newlines,1)
		valid_words.append(newwords[0])
		wordcount+=1
		for word in newwords:
			newlines.remove(word)
		rls,lnks=calculate(valid_words)
		isOK = checkPuzzle(lnks)
		# zprint(wordcount)
	# zprint("in main:lnks,rls:",lnks,rls)
	if(not isOK):
		print("Failed.Current wordcount,valid_words:",wordcount,valid_words)
	#print("valid_words:",valid_words)
	#print(rls,lnks,sts)
	else:
		paths = findPath(lnks,rls)
		print(valid_words)
		print(paths)
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
	# links=[{1},{0,2,3},{1,4},{1,2}]
	# rls = [{'e','b'},{'e','b','s','t'},{'e','s'},{'e','t'}]
	# paths=findPath(links,rls)
	# print(paths)
