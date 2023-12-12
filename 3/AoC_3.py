#def findPartNumber(readline,prevline,nextline):
numberList = ['0','1','2','3','4','5','6','7','8','9']
symbolList = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','\\','/']
readline = '.......................153..988....502..842.........588.....441.468......481..........314...715.57............................163..992..512.'
startNum = ''
numberCheck = []
numberCount = []
numberParse = []
splitNums = []
partDict = {}
lastPlusOne = -5
numberParse = readline.split('.')
for i in numberParse:
	if i != '':
		splitNums.append(i)
print(splitNums)
for position in range(0, len(readline),1):
	if readline[position] in numberList:
		numberCheck.append(str(position))
print(numberCheck)
for number in numberCheck:
	numMinOne = int(number)-1
	numPlusOne = int(number)+1
	print(numMinOne,numPlusOne)
	if numMinOne == lastPlusOne and lastPlusOne != -5:
		numberCount.append(numMinOne)
	if int(number) not in numberCount:
		numberCount.append(int(number))
	if numMinOne not in numberCount:
		numberCount.append(numMinOne)
	if numPlusOne not in numberCount:
		numberCount.append(numPlusOne)
	lastPlusOne = numPlusOne

numberCount.sort()
print(numberCount)

for val in range(0, len(splitNums),1):
	popAmt = len(splitNums[val])+2
	print(popAmt)
	partDict[splitNums[val]] = numberCount[0:popAmt]
	del numberCount[0:popAmt]
print(partDict)

#NEXT: LOOP THROUGH DICTIONARY VALUES AS LINE POSITIONS -- IF SYMBOL IN SYMBOL LIST, ADD KEY TO RESULT 













'''def readText(lineNum):
	if lineNum == 0:
		lineNum = blankLine
	with open('AoC_3_input.txt') as f:
		content = f.readlines()
	return content[lineNum]'''
