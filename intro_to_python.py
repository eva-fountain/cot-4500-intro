# Eva Fountain
# COT4500, Spring 2023
# Intro to Python

import numpy as np

# Number 1
for i in range(0,3):
    for j in range(0,3):
        if(i == j):
            print("1", sep=" ",end=" ")
        else:
            print("0", sep=" ",end=" ")
    print()
print()

# Number 2
for i in range(0,3):
    for j in range(0,3):
        if(i == j):
            print("1", sep=" ",end=" ")
        else:
            print("3", sep=" ",end=" ")
    print()
print()

# Number 3
arr = np.matrix = ([[1, 3, 3],
                    [3, 1, 3],
                    [3, 3, 1]])
print(np.delete(arr, 2, 1))