# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and outputs the last position in the search string
# where the target string appears, or -1 if there
# are no occurences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last(targetString,searchString):
	if targetString.find(searchString) == -1:
		return -1
	else:
		value = len(targetString)
		count = 0
		while count != value:
			if(targetString[count] == searchString):
				count += 1
				print count
				value2 = count
		return value2

print find_last('aaa', 'a')