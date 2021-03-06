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


	def getListOfFilledValues(self):
		values = []
		for item in self.listcell:
			if item.getValue() != 0:
				values.append(item.getValue())
		return values



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

def getXPosGrid(r,c,itr):
	if itr < 50 or itr >= 100:
		return c/3 + 3*(r/3)
	else:
		return r/3 + 3*(c/3)

def getYPosGrid(r,c,itr):
	if itr < 50 or itr >= 100:
		return c%3 + 3*(r%3)
	else:
		return r%3 + 3*(c%3)

def getXPosCol(r,c,itr):
	if itr < 100 :
		return c
	else:
		return c%3 + 3*(r%3)

def getYPosCol(r,c,itr):
	if itr < 100 :
		return r
	else:
		return c/3 + 3*(r/3)


def playGame(game):

	(rlist, clist, glist) = createTable(game)
	print 'The Sudoku grid is:'
	drawTable(rlist)
	allValues = [i for i in range(1,10)]
	iteration = 0
	numScan = 0

	while checkIfTableFull(rlist) is False:

		iteration += 1
		
		#switch to column
		if iteration == 50:
			print 'Switching to column scan'
			temp = clist
			clist = rlist
			rlist = temp

		#switch to grid
		elif iteration == 100:
			print 'Switching to grid scan'
			temp = clist
			clist = rlist
			rlist = glist
			glist = temp

		elif iteration == 150:
			print 'Switching back to row scan'
			iteration = 0
			numScan += 1
			temp = glist
			glist = rlist
			rlist = temp

		#make sure you're not caught in an infinite loop if algorithm fails
		if numScan == 10:
			print 'Couldnt solve game. The unsolved grid is:'
			if iteration < 50:
				drawTable(rlist)
			elif iteration >= 50 and iteration < 100:
				drawTable(clist)
			else:
				drawTable(glist)
			return False


		#scan rows one by one
		for i in range(9):
			if rlist[i].checkIfFull is True:
					continue

			#update predicted values for all cells in row
			for j in range(9):

				#if cell is empty
				if rlist[i].getValueFromCell(j) == 0:
					notPossibleVals = rlist[i].getListOfFilledValues() + clist[getXPosCol(i,j,iteration)].getListOfFilledValues() + \
					glist[getXPosGrid(i,j,iteration)].getListOfFilledValues()
					possibleVals = list(set(allValues) - set(notPossibleVals))


					#if only one value in possibleVals, assign it to cell
					if len(possibleVals) == 1:
						#print 'Assigning value', possibleVals[0], 'to',rlist[i].getID(),'position',j
						rlist[i].assignValueToCell(possibleVals[0], j)
						clist[getXPosCol(i,j,iteration)].assignValueToCell(possibleVals[0], getYPosCol(i,j,iteration))						
						glist[getXPosGrid(i,j,iteration)].assignValueToCell(possibleVals[0], getYPosGrid(i,j,iteration))
						
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
							rlist[i].assignValueToCell(elem, key)
							clist[getXPosCol(i,key,iteration)].assignValueToCell(elem, getYPosCol(i,key,iteration))
							glist[getXPosGrid(i,key,iteration)].assignValueToCell(elem, getYPosGrid(i,key,iteration))

								

	print 'The solved Sudoku grid is:'	
	if iteration < 50:				
		drawTable(rlist)
	elif iteration < 100:
		drawTable(clist)
	else:
		drawTable(glist)
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

#playGame(gamelist[5])
gamesWon = 0
gamesPlayed = 0
for game in gamelist:
	gamesPlayed += 1
	print 'Game', gamesPlayed,'is being played'
	res = playGame(game)
	if res is True:
		gamesWon += 1

print gamesWon,'/ 50 games won.',









