#!/usr/bin/python
#Slice Based Testing

#S30: S(bracket, 35) = {3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}
def get_bracket(inc):
	bracket = 0
	if (0 < inc <= 20000):
		bracket = 1
	elif (20000 < inc <= 30000):
		bracket = 2
	elif (30000 < inc <= 40000):
		bracket = 3
	elif (40000 < inc <= 50000):
		bracket = 4
	elif (50000 < inc <= 90000):
		bracket = 5
	else:
		bracket = 6
		
	return bracket

#S37: S(tax, 33) = {3, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}
def switch(inc, x):
	if x == 1:
		tax = inc * .04
	elif x == 2:
		tax = inc * .05
	elif x == 3:
		tax = inc * .06
	elif x == 4:
		tax = inc * .07
	elif x == 5:
		tax = inc * .10
	elif x == 6:
		tax = inc * .13
	else:
		print "something is wrong with the income bracket computation"
	return tax

#S38: S(tax, 35) = S30 U S37 U {35}
def get_income_tax(inc):
	return switch(inc, get_bracket(inc))

#S43: S(tax, 46) = S38 U {3, 37, 38, 39, 40, 41, 42, 43, 44}
def get_adjusted_tax(tax, dep):
	if (dep == 1):
		tax = tax - (.1 * tax)
	elif (2 <= dep <= 3):
		tax = tax - (.25 * tax)
	elif (3 < dep):
		tax = tax - (.4 * tax)
	else:
		tax = tax
		
	return tax

#S15: S(inc, 48) = {3}
#S22: S(dep, 48) = {3}
#S44: S(tax, 48) = S38 U {3, 37, 38, 39, 40, 41, 42, 43, 44}
def calc_tax(inc, dep):
	tax = get_adjusted_tax(get_income_tax(inc), dep)
	
	print "income = {0} dependent = {1} tax = {2}".format(inc, dep, tax)
	
	return (inc, dep, tax)
