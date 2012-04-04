#Same Structure

#Define a procedure, same_structure, that takes two inputs. It should output
#True if the lists contain the same elements in the same structure, and False
#otherwise. Two values, p and q have the same structure if:

#    Neither p or q is a list.

#    Both p and q are lists, they have the same number of elements, and each
#    element of p has the same structure as the corresponding element of q.


#For this procedure, you can use the is_list(p) procedure from Homework 6:

def is_list(p):
    return isinstance(p, list)

def depth(l):
	return sum(1 + depth(item) if isinstance(item,list) else 1 for item in l)


def same_structure(a,b):
	if (is_list(a)) == False and (is_list(b)) == False:
		return True
	if (is_list(a)) == True and (is_list(b)) == True:
		if depth(a) == depth(b):
			return True
		return False




#Here are some examples:

print same_structure(0,[])

print same_structure(3,7)
#>>> True

print same_structure([1, 0, 1], [2, 1, 2])
#>>> True

print same_structure([1, [0], 1], [2, 5, 3])
#>>> False

print same_structure([1, [2, [3, [4, 5]]]], ['a', ['b', ['c', ['d', 'e']]]])
#>>> True

print same_structure([1, [2, [3, [4, 5]]]], ['a', ['b', ['c', ['de']]]])
#>>> False