# coding:utf-8

def transFile (fromFile, toFile):
	fromF = open (fromFile, 'r')
	toF=open(toFile,'w')

	while True:
		line = fromF.readline ()
		s=line.find('有限公司')
		if s>0 and len(line)<100:
			toF.write(line)
		if not line:
			break

	fromF.close()
	toF.close()

transFile("test.txt","testOut.txt")


