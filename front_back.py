def front_back(a, b):
  # +++your code here+++
  length_a = len(a)
  length_b = len(b)

  print length_a,length_b

  if length_a%2 == 0:
    front_a = a[0:(length_a/2)]
    back_a = a[length_a/2:]

  if length_b%2 == 0:
    front_b = b[0:(length_b/2)]
    back_b = b[length_b/2 :]

  if length_a%2 != 0:
    front_a = a[0:length_a/2+1]
    back_a = a[length_a/2+1:]

  if length_b%2 != 0:
    front_b = b[0:length_b/2+1]
    back_b = b[length_b/2+1:]
  
  return front_a + front_b + back_a + back_b

print front_back('abcde','xyz')

print front_back('Kitten', 'Donut') #KitDontenut