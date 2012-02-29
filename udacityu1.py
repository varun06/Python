p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

# function sense is define here, it takes two parameters
def sense(p, Z):
	q = [ ]
	for i in range(len(p)):
		hit = (Z == world[i])
		q.append(P[i] * (hit * pHit + (1-hit) * pMiss))
		#First, compute the sum of vector q, using the sum function
	s = sum(q)
	for i in range (len(p)):#normalize by going through all the elements in q and divide by s
		q[i]=q[i]/s
	return q
	print sense(p, Z)