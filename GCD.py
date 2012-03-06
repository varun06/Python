def GCD(p,q):
	if q == 0:
		return p
	else:
		return GCD(q,p%q)

print GCD(36,20)