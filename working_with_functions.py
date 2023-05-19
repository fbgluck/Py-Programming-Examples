# functions
# ref: https://www.programiz.com/python-programming/function
# define a function
# The program consists of calling each function
# Author: Fredric Gluck
# ------------------------------
# Variables


# Functions
def mr_glucks_function(x):
    result = ((2*x)-8)**(2/3)
    return result
# End of Function

# Define a  basic function to calculate the area of a rectangle
# Arguments: length and width of the field


def fn_field_area(area_length, area_width):
    return (area_length * area_width)


def absolute_value(num):
    # The following is a doc string. It is used to
    # document the purpose of a function.
    # from the Python interpreter, type -- print (absolute_value.__doc__)
    """This function returns the absolute
    value of the entered number"""

    print("\nAbsolute Value Function")
    if num >= 0:
        return num
    else:
        return -num
# End of the function because the next line is not indented

# A fancier version of the absolute value function


def fancy_av(prompt, num):
    print("\nFancy Absolute Value Function")
    if num >= 0:
        x = prompt + " " + str(num)
        return x
    else:
        return -num


# ----------End of Function Defs ----------------------------
#  Main Program Starts Here
print("Mr. Gluck's Function")
for i in range(0, 11):
    print(f"The input is: {i}....The result is {mr_glucks_function(i)}")
input("Enter to continue ...")
print(30*'-')


# Ask the user for the length and width
# Call the function and return the value
user_length = int(input("What is the length of the field? >> "))
user_width = int(input("What is the width of the field? >> "))
print(f'Calling function from main program')
# We call the function here
total_area = fn_field_area(user_length, user_width)
print(f'We are back in the main program')
print(f'The area of the field is: {total_area}')
print(30*'-')
input('Enter to continue....')
# Now we will call the other functions
print(fancy_av("\nThe absolute value is: ", 2))
print(absolute_value(-4))
