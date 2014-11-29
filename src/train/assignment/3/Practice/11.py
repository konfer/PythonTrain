#coding:utf-8

wordList=list()

def mapFile(file,newFile=True):
	outPutFile=file if newFile else '11outPutFile'
	# map(dropBlankFunc,open(file) )
	#for line in open(file):
		#outPutFile.write(dropBlankFunc(line))
		#toFile.write(dropBlankFunc(line))
	map(dropBlankFunc,open(file))
	toFile=open(outPutFile,'w')
	[toFile.write(line) for line in wordList]


def dropBlankFunc(line):
	wordList.append(filter(isBlank,line))

def isBlank(word):
	return not word.strip()==''


mapFile("gettysburg.txt",False)












