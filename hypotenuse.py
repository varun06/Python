import math

def hypotenuse(a, b):
	asquare = a * a
	bsqaure = b * b
	sumofab = asquare + bsqaure
	result = math.sqrt(sumofab)
	return result

print hypotenuse(3,4)