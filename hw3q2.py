# def proc(p):
# 	p[0] = p[1]
# 	print p

# def proc(p):
# 	p=p+[1]
# 	print p

# def proc(p):
# 	q=p
# 	p.append(3)
# 	print p
# 	q.pop()
# 	print p
# 	print q

def proc(p):
	q = []
	while p:
		q.append(p.pop())
	while q:
		p.append(q.pop())
	print p
	print q

p=[1,2,3]
proc(p)