'''
Create a 2D list of space 5x5 filled with zeroes. 
Take in three coordinates (row and column) from the user. 
Modify the list to store 1s in the space of the entered coordinates. 
Print out resulting matrix. 
Your printed matrix must be formatted like the screenshot below, so if we entered the same input into your program, we should get the same output 
(pay attention to the orientation of the rows and columns here).

'''
# Create a 5x5 matrix filled with zeroes
matrix = [[0] * 5 for _ in range(5)]

# Take user input for three coordinates (row and column)
for i in range(3):
    row = int(input(f"Enter row for coordinate {i + 1}: "))
    col = int(input(f"Enter column for coordinate {i + 1}: "))

    # Modify the list to store 1s in the space of the entered coordinates
    matrix[row - 1][col - 1] = 1

# Print out resulting matrix
for row in matrix:
    print(" ".join(map(str, row)))

# Ext source used: https://stackoverflow.com/questions/60019226/creating-a-matrix-in-python-with-a-range-of-numbers
#                  https://wiki.python.org/moin/ForLoop
    
    