'''
For this exercise, accept a string input from the user and pass that input to a function. 

That function should count the lowercased letters 
(and only the letters, meaning we ignore anything not a letter and treat each letter as lowercase regardless of its actual case) 
of the string in a dictionary and then return that dictionary. 
Print out the resulting dictionary returned by the function.


'''
#Design of the function
def count_lowercase_letters(input_string):
    # Initialize dictionary, which is empty, to store letter counts
    letter_counts = {}

    # Count lowercase letters in the string
    for char in input_string:
        if char.isalpha():  # To determine if the character is a letter
            lowercase_char = char.lower()  # Convert to lowercase
            letter_counts[lowercase_char] = letter_counts.get(lowercase_char, 0) + 1 # Update the count of the lowercase character in the letter_counts dictionary, incrementing by 1 or 
                                                                                     # initializing to 1 if the character is not present.


    return letter_counts

# Take user input for a string
user_input_string = input("Enter a string: ")

# Call the function and print the resulting dictionary
result_dict = count_lowercase_letters(user_input_string)
print("Letter Counts:", result_dict)

# ext source: https://www.w3schools.com/python/ref_string_isalpha.asp
            # https://www.programiz.com/python-programming/methods/string/lower