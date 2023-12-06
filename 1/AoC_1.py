def getCal(string):
	i = u = z = 0
	index1 = index2 = 100
	indexWord1 = indexWord2 = 'NULL'
	textNums = ['zero','one','two','three','four','five','six','seven','eight','nine']
	revTextNums = ['orez','eno','owt','eerht','ruof','evif','xis','neves','thgie','enin']
	revString = string[::-1]
	while i < 10:
		index = string.find(str(i))
		if index > -1:
			if index <= index1:
				index1 = index
				indexWord1 = 'NULL'
		index = string.find(textNums[i])
		if index > -1:
			if index <= index1:
				index1 = index
				indexWord1 = i
		i+=1

	while u < 10:
		index = revString.find(str(u))
		if index > -1:
			if index <= index2:
				index2 = index

		u+=1
	
	indexWord2 = 'NULL'	
	while z < 10:
		index = revString.find(revTextNums[z])
		if index > -1:
			if index <= index2:
				index2 = index
				indexWord2 = z
		z+=1
	
	if indexWord1 != 'NULL':
		cal1 = indexWord1
	else: 
		cal1 = string[index1]

	if indexWord2 != 'NULL':
		cal2 = indexWord2
	else: 
		index2rev = int(len(string)-index2-1)
		cal2 = string[index2rev]
	cal = str(cal1)+str(cal2)
	return(int(cal))


def readText(lineNum):
	with open('AoC_1_input.txt') as f:
		content = f.readlines()
	return content[lineNum]


calTotal = 0
for i in range(0,1000,1):
	calVal = getCal(readText(i))
	print(calVal)
	calTotal += int(calVal)
print(calTotal)

