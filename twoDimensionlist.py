# 2D list
# vast variety of application of 2D array in ML and Data Science

# 3x3 matrix in maths
# [
#    1 2 3
#    4 5 6
#    7 8 9
# ]

# it can be stored in python as 2D list as follows
# each item in matrix is another list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# accessing first element of matrix
print(matrix[0][0])

for item in matrix:
    print(item) # return list
    # [1, 2, 3]
    # [4, 5, 6]
    # [7, 8, 9]

for item in matrix:
    print(item[0])


# modify first element of matrix
matrix[0][1] = 30
print(matrix[0][1])

# To iterate over each element in matrix
for row in matrix:
    for item in row:
        print(item)  # will return all items in list from 1 to 9

