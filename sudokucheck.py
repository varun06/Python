correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]


def check_sudoku(p):
	n = len(p) # extract the length of list
	digit = 1 # start with 1
	while digit <= n:
		i = 0
		while i<n:
			row_count = 0
			col_count = 0
			j = 0

			while j<n:
				if p[i][j] == digit:
					row_count += 1
				if p[j][i] == digit:
					col_count += 1
				j = j +1
			if row_count !=1 or col_count != 1:
				return False
			i = i +1
		digit = digit + 1
	return True

print check_sudoku(correct)
print check_sudoku(incorrect)
