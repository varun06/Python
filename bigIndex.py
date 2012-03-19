def make_string(p):
	s = ""
	for e in p:
		s = s + e
	return s

def make_big_index(size):
	index = []
	letters = ['a','a','a','a','a','a','a','a']
	while len(index) < size:
		word = make_string(letters)
		add_to_index(index,word,'fake')
		for i in xrange(len(letters) - 1,0,-1):
			if letters[i] < 'z':
				letters[i] = chr(ord(letters[i]) + 1)
				break
			else:
				letters[i] = 'a'
	return index

print make_big_index(10000000)