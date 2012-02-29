x = 100
divisors = ()

for i in xrange(1,x):
	if x%i == 0:
		divisors = divisors + (i,)
print divisors
