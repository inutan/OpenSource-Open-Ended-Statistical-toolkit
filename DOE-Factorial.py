import re

def getNDimensioanlList(nb_lines, n):
	# Returns a list of list. 
	# The length of list is nb_lines. 
	# Length of each inner list is n.
	nDimList = []
	for i in range(0,nb_lines):
		inner_array = []
		for j in range(0,n):
			inner_array.append(0)
		nDimList.append(inner_array)
			
	return nDimList


def stk_fullfact(levels):
	""" 
		Function Name : stk_fullfact()
		Description: TBD
		Input Params: List stating levels. 
					   e.g. The scenario where we have three levels with 
					   2, 3 and 1 variants in each respectively, the levels
					   list would be [2,3,1]  
		Return : Returns the a list of list representing the full factorial
				  For the above example return would be 
				  [	[0, 0, 0], 
					[1, 0, 0], 
					[0, 1, 0],
					[1, 1, 0], 
					[0, 2, 0],
					[1, 2, 0]]	
	"""
	n = len(levels)  # number of factors	e.g levels= [2,3]
	nb_lines = 1
	for level in levels:
		nb_lines *= level 	# for the above example nb_lines will be 2*3 =6

	level_repeat = 1
	range_repeat = nb_lines

	# Get a list of list, with every list member initialied with zero
	# for the above case return a list of size 3*2 with each l=inner list of lenght 2.
	fullFactorial = getNDimensioanlList(nb_lines,n) 
	for i in range(n):
		range_repeat /= levels[i]
		lvl = []
		for j in range(levels[i]):
			lvl += [j]*level_repeat
		rng = lvl*range_repeat
		level_repeat *= levels[i]
		for j in range(0, nb_lines):
			fullFactorial[j][i] = rng[j]
			
	return fullFactorial


if __name__=="__main__":
	levels = [2,3,1]
	print stk_fullfact(levels)
	
# your code goes here