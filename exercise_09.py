'''
Accept 5 integer inputs from the user and print the sum. 
Different in this exercise is that you cannot trust the user, just like in real life. 
You must validate that the input is actually an integer and cannot rely on the user always entering integers. 
If the user enters something other than a valid integer, print an error message and make them enter the number again until they enter 5 integers and you can print the sum.

'''

# Function to validate and get integer input from the user. 
def get_integer_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError: # prints an error message if something is entered other than a valid integer
            print("Invalid input. Please enter an int.")

# Initialize sum variable
total_sum = 0

# Get 5 integer inputs from the user
for i in range(5):
    user_number = get_integer_input(f"Enter integer {i + 1}: ")
    total_sum += user_number

# Print the sum
print("Your sum is", total_sum)
