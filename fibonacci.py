def fibonacci(n):
	'''a small function to compute fibonacci'''
	# base case, when n is 0 or 1
	if n == 0 or n == 1:
		return 1
	else:
		# when n in not 0 or 1
		return fibonacci(n-1) + fibonacci(n-2)

print fibonacci(4)