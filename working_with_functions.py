#functions 
# ref: https://www.programiz.com/python-programming/function
# define a function
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
#End of the function because the next line is not indented

def fancy_av (prompt, num):
    print ("\nFancy Absolute Value Function")
    if num >= 0:
        x = prompt + " " + str(num)
        return x
    else:
        return -num

print(fancy_av("\nThe absolute value is: ",2))
print(absolute_value(-4))