#Define a procedure, product_list,
#takes as input a list of numbers,
#and returns a number that is
#the result of multiplying all
#those numbers together.

#product_list([9]) => 9
#product_list([1,2,3,4]) => 24

def product_list(inputList):
	result = 1
	for a in inputList:
		result *= a
	print result

inputList1 = [9]
inputList2 = [1,2,3,4]

product_list(inputList1)
product_list(inputList2)
    
