###############################################################################
"""	
@author		: Nutan Kumari
@filename	:	DOE-Factorial.py
@brief		: This file provides the implementation for common 
			  functions  for DOE Factorial.
@functions	:  
	1.	OSOEST_fullfact()	:	Provides implementation for Full Factoorial
	2.	OSOEST_ff2n()		: 	Provides implementation for 2-Level 
								full-factorial 
	3.	OSOEST_fracFact()	:	Provides implementation for fractional 
								factorial
@version	:	v1.0
@date		:	29 Jan 2015
"""
###############################################################################

import re


"""
@function		: getNDimensioanlList
@brief			: Helper function used by OSOEST_fullfact()
@processing		:	TBD 	
"""
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

""" 
@function		: OSOEST_fullfact()
@brief			: Provides implementation for OSOEST_fullfact API function
@processing		:	
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
def OSOEST_fullfact(levels):
	
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

"""
The following main function should be used for unit testing this 
module
"""
if __name__=="__main__":
	levels = [2,3,1]
	print OSOEST_fullfact(levels)
	
# your code goes here