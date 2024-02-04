'''
Take in a number, n, from the user. 
# Then, take in n integers from the user and store them in a list. 
# For instance, if the user enters 4, then the user will have to enter 4 numbers.
# Print the list and the median of the list (in the case where there is no middle element pick any of the two middle elements). 
# Do not use any modules, neither standard library nor third party -- global "built-in" functions are allowed however.

'''


# Take user input for the number of integers, n
n = int(input("Enter the number of integers: "))

# Take user input for n integers and store them in a list
integer_list = [int(input(f"Enter integer {i + 1}: ")) for i in range(n)]

# Print statement for list of
print("List of integers:", integer_list)

# Sort the list from smallest to largest
integer_list.sort()

# Calculate the median and special case where there is no middle element
middle_element = n // 2
median = (integer_list[middle_element - 1] + integer_list[middle_element]) / 2 if n % 2 == 0 else integer_list[middle_element]

# Print the median
print("Median of the list:", median)