import time
# def product(p):
	
# 	result = 1
# 	for e in p:
# 		result = result * e
# 	return result

# def find_match(p, target):
#     for x in p:
#         for y in p:
#             if x * y == target:
#                 return True
#     return False


def tricky_loop(p):
    while True:
        if len(p) == 0:
            break
        else:
            if p[-1] == 0:
                p.pop() # assume pop is a constant time operation
            else:
                p[-1] = 0
    return 101
	

p = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
start_time = time.time()
print tricky_loop(p)
print time.time() - start_time,"seconds"