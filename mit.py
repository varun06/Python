#initialize the variable
x = -16
# initialize variable ans
ans = 0
if x>=0:
	while ans*ans < x: # while loop to iterate
		ans = ans + 1
	if ans*ans !=x:
		print x, 'is not a perfect square'
	else: print ans
else:print x, 'is a negative number'
