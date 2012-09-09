t = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

def inBucket(t, low, high):
	count = 0 
	for num in t:
		if low < num < high:
			count += 1
	return count

numBuckets = 8
buckets = [0] * numBuckets
bucketWidth = 1.0 / numBuckets
for i in range(numBuckets):
	low = i * bucketWidth
	high = low + bucketWidth
	buckets[i] = inBucket(t, low, high)
print buckets