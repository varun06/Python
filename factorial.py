def factorial(n):
	'''A small function to return factorial of a number'''

	# verify the type of parameter - should be an int
	if not isinstance(n, int):
		print "Factorial is only defined for integers."
		return -1
	elif n<0:
		# if value is less than 0, return -1
		print "Factorial is only defined for positive integers."
		return -1
	# Base case - when n == 0
	if n == 0:
		return 1
	else:
		# when n is not 0 
		return  n * factorial(n-1)

print factorial(2.5) # should be 120