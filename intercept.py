def slope(x1, y1, x2, y2):
	dy = y2 - y1
	dx = x2 - x1
	m = dy/dx
	return m

def intercept(x1, y1, x2, y2):
	m = slope(x1, y1, x2, y2)
	return (y2 - m * x2)

print intercept(3,5,9,11)