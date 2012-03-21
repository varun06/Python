def bad_hash_string(keyword,buckets):
	return ord(keyword[0])%buckets

print bad_hash_string('u',5)