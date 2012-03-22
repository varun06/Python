import time

# def sum_list(p):
#     sum = 0
#     for e in p:
#         sum = sum + e
#         run_time = time.clock()
#     print run_time
#     return sum

# p = [1,2,3,4,5,6,7,8,9,10,11,12,12,13,14,15,16,17,18]
# print sum_list(p)

def has_duplicate_element(p):
   res = []
   for i in range(0, len(p)):
       for j in range(0, len(p)):
           if i != j and p[i] == p[j]:
               return True
        run_time = time.clock()
   return False
   print run_time

p = [1,2,3,4,5,6,7,8,9,10,11,12,12,13,14,15,16,17,18]
print has_duplicate_element(p)