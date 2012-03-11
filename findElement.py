#Define a procedure, find_element,
#that takes as its inputs a List
#and a value of any type, and
#outputs the index of the first
#element in the input list that
#matches the value.

#If there is no matching element,
#output -1.

#find_element([1,2,3],3) => 2

#find_element(['alpha','beta'],'gamma') => -1

# def find_element(inputList,item):
# 	value = 0
# 	for i in xrange(len(inputList)):
# 		if item == inputList[i]:
# 			return i
# 	return -1
	
			


def find_element(inputList,item):
	if item in inputList:
		return inputList.index(item)
	else:
		return -1

print find_element([1,2,3],3)
print find_element(['alpha','beta'],'gamma')

