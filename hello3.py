matrix =[[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
print([[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))])

print()

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[:]
print(a)
del a
