# coding:utf-8

def showProp (file):
	lineNum = 0
	for line in open (file):
		lineNum += len (line)
		yield line
	print "gettysburg.txt中单词个数为：" + str (lineNum)


p = showProp ("gettysburg.txt")
dict={}
for line in p:
	print line
	for w in line:
		if w in dict:
			dict[w]+=1
		else:
			dict[w]=1

myKeys=dict.keys()

print "存在字母个数："+str(len(myKeys))


for key in myKeys:
	if key !='':
		print "gettysburg.txt存在字母"+str(key)+",出现次数："+str(dict[key])

