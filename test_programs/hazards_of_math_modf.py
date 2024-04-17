# This is an experiment to show what happens to precision
# of a floating point number when attempting to find the decimal part and
# fractional part using math.modf()
# You should read this article to undertstand more about
# how floating point numbers are represented inside a machine
# and why this may (or may not) be a problem
# https: // docs.python.org/3/tutorial/floatingpoint.html
import math
from decimal import Decimal
test_amount = input("Enter a number with two decimal places: ")
print(f"You Entered the string: {test_amount}")
float_amount = float(test_amount)
print(f"Conversion to float gives {float_amount}")
print(f"Math.modf returns a tuple as: {math.modf(float_amount)}")
fraction_part, integer_part = math.modf(float_amount)
print(f"Fractional part = {fraction_part}")
# decimal_part = Decimal(fraction_part)
print(f"Integer Part = {integer_part}")
print(
    f"Multiply fractional part by 100 to get decimal part: {int(fraction_part *100)}")
print(f"Forcing integer_part to integer is: {int(integer_part)}")
print("*"*5, " Using String Slicing and Int Conversion ", "*"*5)
print(
    f"The last two sliced characters of string input are: {test_amount[-2:]}")
fraction_part = int(test_amount[-2:])
print(f"Fraction part of input string converted to int is: {fraction_part}")
