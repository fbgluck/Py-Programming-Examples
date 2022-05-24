# Sample try / except / else used to handle errors
#
# This shows a reasonable way to handle errors that are
# raised in Python.
#
# ref: https://www.programiz.com/python-programming/exceptions
# ref: https://docs.python.org/3/library/exceptions.html

print("Start test...")
try:  # This is the code that will be executed
    x = input(" Enter a letter (to throw an error) or a number: ")
    x = int(x)  # This will throw an error if a string is entered

except Exception as e:  # Optional: Uses the Exception object that is created
    # when a system occurs
    # If an error occurs in the try part, the
    # code in the except part will be executed
    print("Exception: Sorry Dave... I can't do that")
    print("Did you enter a letter when you should have entered a number?")
    print(f"Oops! {e.__class__} occurred.")  # Print the type of error
    print(f"For more info, see https://docs.python.org/3/library/exceptions.html")
    # print(e.message) # Use this for lots more detail

else:   # If the code in try does not throw an error
    # the code in else is executed
    print(f"Coversion was successful: x={x}")
finally:    # This code is executed regardless
    # of the result of the code in try
    print(f" \n*** This is the code in finally ***")
