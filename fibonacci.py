#Define a procedure, fibonacci, that takes a natural number as its input, and
#returns the value of that fibonacci number.

#Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

#Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
	if n==0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1)+fibonacci(n-2)

def fibonacciiter(n):
	previousValue = 0
	currentValue = 1
	value = 1
	index = 1
	if n == 0:
		return 0
	if n == 1:
		return 1
	while(index<n):
		value = previousValue + currentValue
		previousValue = currentValue
		currentValue = value
		index += 1
	return value

	def fibonacciiter2(n):
    current = 0
    after = 1
    for i in range(0,n):
        current,after = after,current+after
    return current



print fibonacciiter(0)
#>>> 0
print fibonacciiter(1)
#>>> 1
print fibonacciiter(15)
#>>> 610
print fibonacciiter(36)
#>>>14930352