import math # import math module

def printLog(n):
	n = float(n)
	while n > 0:
		print n, '\t', math.log(n)
		n = n - 1

def printLog1(n):
	n = float(n)
	while n > 0:
		print n, '\t', math.log(n)/math.log(2)
		n = n - 1

print printLog(10)
print printLog1(10)