#Prefix Removal


#Define a procedure, remove_prefix, that takes as input a string, and returns a
#string that is the part of the string following the first hyphen -. If the input string does
#not contain any hyphen -, remove_prefix should return the full input string.

def remove_prefix(s):
	prefix_position = s.find('-')
	return s[prefix_position + 1:]



#For example,

print remove_prefix('super-udacity')
#>>> 'udacity'

print remove_prefix('counter-counter-intelligence')
#>>> 'counter-intelligence'

print remove_prefix('antigravity')
#>>> 'antigravity'

print remove_prefix('')
