
# take a 3x3 matrix
import numpy as np
A = [[15, 9, 3],
     [4, 5, 6],
     [7, 8, 9]]

# take a 3x4 matrix
B = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 6, 9, 1]]

result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

# iterating by row of A
for i in range(len(A)):

    # iterating by column by B
    for j in range(len(B[0])):

        # iterating by rows of B
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

for r in result:
    print(*r)

# new method using numpy

# take a 3x3 matrix
A = [[15, 9, 3],
     [4, 5, 6],
     [7, 8, 9]]

# take a 3x4 matrix
B = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 6, 9, 1]]

# result will be 3x4

result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

result = np.dot(A, B)

for r in result:
    print(r)
