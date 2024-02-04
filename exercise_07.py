'''
Take in a string from the user and split it into an array of single characters. 
Split the list of characters into a list of lists where each inner list has 3 elements. 
Notice that the last inner array may have fewer than 3 elements.

'''

# Take user input for any string
user_input_string = input("Enter a string: ")

# Split the string into an array of single characters
characters_list = list(user_input_string)

# Split the list of characters into a list of lists with 3 elements each
lists_of_three = [characters_list[i:i + 3] for i in range(0, len(characters_list), 3)]

# Print the list of characters, and the list of lists
print("List of Characters:", characters_list)
print("List of Lists with 3 Elements Each:", lists_of_three)
