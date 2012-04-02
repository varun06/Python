def is_palindrome(s):
	if (len(s) < 2):
		return True
	
	if(s[0] != s[-1]):
		return False
	else:
		return is_palindrome(s[1:-1])

def is_palindromeiter(s):
	for i in xrange(0,len(s)/2):
		if(s[i] != s[-(i+1)]):
			return False
		return True
	

print is_palindrome('level')
print is_palindromeiter('level')