#Define a procedure, greatest,
#that takes as input a list
#of positive numbers, and
#returns the greatest number
#in that list. If the input
#list is empty, the output
#should be 0.

#greatest([4,23,1]) => 23
#greatest([]) => 0

def greatest(inputList):
	maxNumber = 0
	if inputList == []:
		return 0
	else:
		for num in inputList:
			if num > maxNumber:
				maxNumber = num
		return maxNumber


print greatest([4,23,1])
print greatest([])


    


    
