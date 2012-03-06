def fib(x):
	if x == 0 or x == 1: return 1
	else:
		return fib(x-1)+fib(x-2)
fib(5)
fib(25)
fib(35)
