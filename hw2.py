# Define a procedure, median, that takes three
# numbers as its inputs, and outputs the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b
        
def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
    lastItem = biggest(a,b,c)
    result1 = 0
    result2 = 0
    if a == lastItem:
        result1 = b
        result2 = c
    if b == lastItem:
        result1 = a
        result2 = c
    if c == lastItem:
        result1 = a
        result2 = b
        # print result1
        # print result2
    med = bigger(result1,result2)
    return med
    
print median(7,8,7)







