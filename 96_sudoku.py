#Problem 96 - Sudoku


#############################################################
#Part 1 - writing required classes
#write Cell class corresponding to each cell in grid
#############################################################

class Cell():

	def __init__(self):
		self.value = 0	
		self.possibleValues = []

	def clearPossibleValues(self):
		self.possibleValues = []

	#Adding getter and setter methods
	def addPossibleValue(self,val):
		self.possibleValues.append(val)

	def removePossibleValue(self, val):
		self.possibleValues.remove(val)

	def getPossibleValues(self):
		return self.possibleValues

	def assignValue(self,val):
		self.value = val
		self.possibleValues = []

	def getValue(self):
		return self.value


#creating class representing rows, columns and 3x3 grids of 9x9 table
class RCG():

	def __init__(self):
		self.id = 0
		self.listcell = []
		for i in range(0,9):
			self.listcell.append(Cell())
		
	def setID(self, id):
		self.id = id

	def getID(self):
		return self.id

	def getValueFromCell(self, pos):
		return self.listcell[pos].getValue()

	def assignValueToCell(self,val,pos):
		self.listcell[pos].assignValue(val)

	def assignPredictedValuesToCell(self, vals, pos):
		self.listcell[pos].clearPossibleValues()
		for val in vals:
			self.listcell[pos].addPossibleValue(val)

	def getPredictedValuesFromCell(self, pos):
		return self.listcell[pos].getPossibleValues()

	def removePredictedValueFromCell(self, val, pos):
		self.listcell[pos].removePossibleValue(val)

	def checkIfFull(self):
		for item in self.listcell:
			if item.getValue() == 0:
				return False		
		return True

	def checkIfAllPredicted(self):
		for item in self.listcell:
			if len(item.getPossibleValues()) == 0:
				return False
		return True

	def getListOfFilledValues(self):
		values = []
		for item in self.listcell:
			if item.getValue() != 0:
				values.append(item.getValue())
		return values

	def NumCellsFilled(self):
		count = 0
		for item in self.listcell:
			if item.value != 0:
				count += 1
		return count



#####################################################################
#Part 2 - create Table
#####################################################################

def createTable(game):
	#create and fill all rows
	robjlist = []
	for i in range(0,9):
		#r = []
		robj = RCG()
		robj.setID('r'+ str(i+1))
		#print robj.getID()
		for j in range(0,9):
			robj.assignValueToCell(int(game[i][j]), j)
			#r.append(robj.getValueFromCell(j)) 
		robjlist.append(robj)
		del(robj)
		#print r

	#create and fill all columns
	cobjlist = []	
	for i in range(0,9):
		#c = []
		cobj = RCG()
		cobj.setID('c' + str(i+1))
		#print cobj.getID()
		for j in range(0,9):
			cobj.assignValueToCell(int(game[j][i]), j)
			#c.append(cobj.getValueFromCell(j))
		cobjlist.append(cobj)
		del(cobj)
		#print c

	#create and fill all grids
	gobjlist = []
	jstart = 0
	kstart = 0
	for i in range(0,9):
		#g = []
		gobj = RCG()
		gobj.setID('g' + str(i+1))
		#print gobj.getID()
		if i != 0:
			if i%3 == 0:
				jstart += 3
				kstart = 0
			else:
				kstart += 3
		pos = 0 
		for j in range(jstart, jstart + 3):
			for k in range(kstart, kstart + 3):
				gobj.assignValueToCell(int(game[j][k]), pos)
				#g.append(gobj.getValueFromCell(pos))
				pos += 1
		gobjlist.append(gobj)
		del(gobj)
		#print g

	return (robjlist, cobjlist, gobjlist)


#print statement for debugging
def drawTable(rlist):
	for i in range(9):
		print 
		for j in range(9):
			print rlist[i].getValueFromCell(j),
	print


################################################################################
#Part 3 - the Sudoku algorithm
################################################################################

def checkIfTableFull(rlist):
	for i in range(9):
		if rlist[i].checkIfFull() is False:
			return False
	return True


def getCorrespondingGrid(r,c):
	if r >= 0 and r < 3:
		if c >= 0 and c < 3:
			return 0
		elif c >= 3 and c < 6:
			return 1
		else:
			return 2
	elif r >= 3 and r < 6:
		if c >= 0 and c < 3:
			return 3
		elif c >= 3 and c < 6:
			return 4
		else:
			return 5
	else:
		if c >= 0 and c < 3:
			return 6
		elif c >= 3 and c < 6:
			return 7
		else:
			return 8


def playGame(game):

	(rlist, clist, glist) = createTable(game)
	print 'The Sudoku grid is:'
	drawTable(rlist)
	allValues = [i for i in range(1,10)]
	iteration = 0

	while checkIfTableFull(rlist) is False:

		#make sure you're not caught in an infinite loop if algorithm fails
		iteration += 1
		if iteration == 50:
			print 'Couldnt solve game. The unsolved grid is:'
			drawTable(rlist)
			return False

		#scan rows one by one
		for i in range(9):
			if rlist[i].checkIfFull is True:
					continue

			#otherwise, update predicted values for all cells in row
			for j in range(9):

				#if cell is empty
				if rlist[i].getValueFromCell(j) == 0:
					notPossibleVals = rlist[i].getListOfFilledValues() + clist[j].getListOfFilledValues() + \
					glist[getCorrespondingGrid(i,j)].getListOfFilledValues()
					possibleVals = list(set(allValues) - set(notPossibleVals))

					#elements not in alreadyPredicted but present in possibleVals should be 
					#removed from possibleVals
					if len(rlist[i].getPredictedValuesFromCell(j)) > 0:
						alreadyPredicted = rlist[i].getPredictedValuesFromCell(j)
						remove =  set(possibleVals) - set(alreadyPredicted)
						for item in remove:
							possibleVals.remove(item)	
					#print rlist[i].getID(), j, '-', possibleVals

					#if only one value in possibleVals, assign it to cell
					if len(possibleVals) == 1:
						#print 'Assigning value', possibleVals[0], 'to',rlist[i].getID(),'position',j
						rlist[i].assignValueToCell(possibleVals[0], j)
						clist[j].assignValueToCell(possibleVals[0], i)						
						glist[getCorrespondingGrid(i,j)].assignValueToCell(possibleVals[0], (j%3 + 3*(i%3)))
						
						#must remove assigned value from corresponding predicted value
						for k in range(9):
							if possibleVals[0] in rlist[i].getPredictedValuesFromCell(k):
								#print 'Removing', possibleVals[0], 'from', rlist[i].getID(), 'position', k 
								rlist[i].removePredictedValueFromCell(possibleVals[0], k)
						
					#else, assign predicted values to cell
					else:
						rlist[i].assignPredictedValuesToCell(possibleVals, j)
						

			#if values of all cells are already predicted for the particular row					
			allElems = dict()
			for j in range(9):
				if rlist[i].getValueFromCell(j) == 0 : 
					allElems[j] = rlist[i].getPredictedValuesFromCell(j)
			
			#1. go through values to check if any element occurs only once. If yes place it in position
			#and delete it from predicted values of other cells of corresponding column and grid
			occurOnce = []
			listvals = allElems.values()

			#convert list of list to simple list
			vals = [item for sublist in listvals for item in sublist]
			if len(vals) == 0:
				continue
			
			for elem in vals:
				if vals.count(elem) == 1:
					occurOnce.append(elem)

			#if no element occurs just once, go to next iteration
			if len(occurOnce) == 0:
				continue

			else:
				for elem in occurOnce:
					for key in allElems:		
						if elem in allElems[key]:
							#print elem, 'occurs only in', rlist[i].getID(), 'position = ', key
							#print 'Assigning value', elem, 'to',rlist[i].getID(),'position',key
							rlist[i].assignValueToCell(elem, key)
							clist[key].assignValueToCell(elem, i)
							glist[getCorrespondingGrid(i, key)].assignValueToCell(elem, (key%3 + 3*(i%3)))

								

	print 'The solved Sudoku grid is:'					
	drawTable(rlist)
	return True


################################################################################
#Part 4 - Parsing through sudoku.txt to get all 50 games
################################################################################
game = []
gamelist = []
fh = open('sudoku.txt','r')
#start reading from second line of file
next(fh)

for line in fh:
	if line.startswith('Grid'):
		gamelist.append(game)
		game = []
		continue
	else:
		game.append(line.rstrip())

gamesWon = 0
gamesPlayed = 0
for game in gamelist:
	gamesPlayed += 1
	print 'Game', gamesPlayed,'is being played'
	res = playGame(game)
	if res is True:
		gamesWon += 1

print gamesWon,'/50 games won.',









