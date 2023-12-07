
def parseString(string):
	red = blue = green = 0
	minRed = minBlue = minGreen = 0
	possible = 1
	gameNum = (string.split(':')[0]).removeprefix('Game ')
	setSplit = (string.split(':')[1])
	splitList = setSplit.split(';')
	cleanList = [i.replace('\n','') for i in splitList]
	for group in cleanList:
		colorSplit = group.split(',')
		for color in colorSplit:
			if 'red' in color: red = color.removesuffix('red')
			if 'blue' in color: blue = color.removesuffix('blue')			
			if 'green' in color: green = color.removesuffix('green')

			if int(red) > minRed: minRed = int(red)
			if int(blue) > minBlue: minBlue = int(blue) 
			if int(green) > minGreen: minGreen = int(green)  

		if int(red) <= 12 and int(blue) <= 14 and int(green) <=13 and possible == 1:
			possible = 1
		else: possible = 0
		red = blue = green = 0
	minPower = (minRed * minBlue * minGreen)
	if possible == 1:
		return (gameNum, minPower)
	return (0, minPower)


def readText(lineNum):
	with open('AoC_2_input.txt') as f:
		content = f.readlines()
	return content[lineNum]



idSum = idCount = powerSum = 0
for i in range(0,100,1):
	idCount, minPower = parseString(readText(i))
	idSum += int(idCount)
	powerSum += int(minPower)
print('Total ID Sum:' + str(idSum))
print('Total Power Sum:' + str(powerSum))