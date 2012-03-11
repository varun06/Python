#Define a procedure, sum_list,
#that takes as its input a
#List of numbers, and produces
#as its output the sum of all
#the elements in the input list.

#For example,
#sum_list([1,7,4]) => 12

def sum_list(listofnumbers):
	result = 0
	for number in listofnumbers:
		result = result + number
		number = number + 1
	return result

numberlist = [1,7,4,5,9]
print sum_list(numberlist)