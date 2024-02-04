'''
Write a script that takes in two strings from the user.
If one string is the suffix of the other string, print the suffix, otherwise, print "No suffix found". 
For example, if the user enters "brush" and "paintbrush", then the script would print "brush". 
If the user entered "painting" and "painted", the script would print "No suffix found" because no string ends with the other. 
Keep in mind that the the pair "brush" and "paintbrush" as well as the pair "paintbrush" and "brush" would print "brush" because order does not matter.

'''
def find_suffix(str1, str2):
    # This is to check if str1 is a suffix of str2
    if str2.endswith(str1):
        return str1
    
    # This is to check if str2 is a suffix of str1
    elif str1.endswith(str2):
        return str2
    else:
        return "No suffix found"

# Getting user input
input_str1 = input("Enter the first string: ")
input_str2 = input("Enter the second string: ")

# Calls the function and prints response accordingly
result = find_suffix(input_str1, input_str2)
print(result)
  