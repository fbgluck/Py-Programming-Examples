# Age is the age of the customer
age = 23
# Check to see if the customer can be served
if age < 21:
    print("Underage")  # Underaged people can not be served
else:
    print("OK to serve")
# Test to see if a number is even or odd
test = int(input("What is the number you want to test?"))
if test % 2 == 0:
    print("the number", test, "is even")
else:
    print("the number", test, "is odd")


# Order of Operations
a = 5
b = 6
c = 7
# Why do I get different results
print("Without ():", a*b+c)
print("With ():", (a*b)+c)
print("And this:", a*(b+c))
