a = raw_input("Enter the value: ")
myValue = int(a)
for i in range (1, myValue):
	if i%15==0:
		print "FizzBuzz"
	elif i%5==0:
		print "Buzz"
	elif i%3==0:
		print "Fizz"
	else:
		print i