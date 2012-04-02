def deep_count(l):
        return sum(1 + deep_count(item) if isinstance(item,list) else 1 for item in l)

print deep_count([[[[[[[[1, 2, 3]]]]]]]])
print deep_count([1, [1, 2, [3, 4]]])