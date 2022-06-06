import numpy as np
m = [[0, 1], [2, 3], [4, 5]]
for row in m:
    print(row)
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print("\n")
for row in rez:
    print(row)

# using numpy
matrix = np.array([[0, 1], [2, 3], [4, 5]])
print(matrix, '\n')
print(matrix.T, '\n')
print(np.transpose(matrix))
