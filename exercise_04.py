'''
Take in 5 integers from the user and store them in a list. 
Then take in another 5 integers and store them in a separate list. 
Create a third array containing just the common values from both arrays without storing duplicates. 
Print out all three lists.

'''
# Take user input for the first list of 5 integers
list1 = [int(input("Enter a number for the first list: ")) for _ in range(5)]

# Take user input for the second list of 5 integers
list2 = [int(input("Enter a number for the second list: ")) for _ in range(5)]

# Create a third list containing common values without duplicates
common_values = list(set(list1) & set(list2))

# Print all three lists
print("List 1:", list1)
print("List 2:", list2)
print("Common Values:", common_values)

# Ext source used: https://www.geeksforgeeks.org/python-print-common-elements-two-lists/
