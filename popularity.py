def popularity(t,p):
	if t == 0:
		return 1
	else:
		score = 0
		for f in friends(p):
			score = score + popularity(t-1,p)
		return score


friends = ['Alice','Bob','Edgar']
print popularity(5,friends)