'''
Take in 10 integers from the user and store them in a list. 
Create a new list with only elements which appear twice. 
Print both lists.
'''
# Take user input for 10 integers
user_input_list = [int(input(f"Enter integer {i + 1}: ")) for i in range(10)]

# Create a new list with elements that appear twice
duplicates_list = [item for item in set(user_input_list) if user_input_list.count(item) == 2]

# Print both lists
print("Original List:", user_input_list)
print("List with Elements Appearing Twice:", duplicates_list)

# ext. source: https://www.geeksforgeeks.org/python-program-print-duplicates-list-integers/