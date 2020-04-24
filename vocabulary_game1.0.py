import random
def zuo(xxx,a,repeat_letter):
	a_len=len(a)
	num=a_len-1
	xxx=xxx.replace(a[repeat_letter],"=")
	xxx_len=len(xxx)
	cover_xxx_letters_count=xxx_len//3
	random_xxx_len=xxx_len-1
	for w in range(cover_xxx_letters_count):
		cover_xxx_letters=random.randint(0,random_xxx_len)
		while xxx[cover_xxx_letters]=="=":
			cover_xxx_letters=random.randint(0,random_xxx_len)
		xxx=xxx.replace(xxx[cover_xxx_letters],"/")
	return(xxx)

w="ket.txt"
file=open(w,"r")
alllines=file.readlines()
file.close()
linecount=len(alllines)
for v in range(linecount):
	alllines[v]=alllines[v].replace("\n","")
while True:
	the_line=random.randint(1,linecount)
	write=alllines[the_line-1]
	if len(write)==1:
		continue
	test_write=write
	test_write=test_write.replace(" ","")
	test_write=test_write.replace(".","")
	test_write=test_write.replace("/","")
	test_write=test_write.replace("(","")
	test_write=test_write.replace("!","")
	if test_write==write:
		first_word=write
		#now_first=write
		break
while True:
	the_line=random.randint(1,linecount)
	write=alllines[the_line-1]
	if len(write)==1:
		continue
	test_write=write
	test_write=test_write.replace(" ","")
	test_write=test_write.replace(".","")
	test_write=test_write.replace("/","")
	if test_write==write:
		second_word=write
		a=[]
		for i in second_word:
			if i in first_word:
				#now_first=first_word.replace(i,"")
				a.append(i)
		if first_word!=second_word and len(a)!=0:
			break
a_len=len(a)
num=a_len-1
repeat_letter=random.randint(0,num)
first_word_last=zuo(first_word,a,repeat_letter)
second_word_last=zuo(second_word,a,repeat_letter)
print(first_word_last)
print(second_word_last)
ans=input("")
print(first_word)
print(second_word)