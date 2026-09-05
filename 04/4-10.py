# 4-10. Slices: Using on of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
#   * Print the message 'The first three items in the list are:'. Then use a slice to print the first three items of that program's list.
#   * Print the message 'Three items from the middle of the list are:'. Then use a slice to print the first three items from the middle of the list.
#   * Print the message 'The last three items in the list are:'. Then use a slice to print the last three items in the list.
# --------------------------------------------------------------------------------------------------------------------------------------------------

languages = ['python', 'javascript', 'c++', 'ruby', 'react']

print(f"The first three items in the list are: {languages[:3]}")
print()

print(f"Three items from the middle of the list are: {languages[1:4]}")
print()

print(f"The last items in the list are: {languages[-3:]}")
print()
