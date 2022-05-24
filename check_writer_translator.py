# This is a program that will translate a number into
# its English equivalent that can be used when writing
# a check
# *********************************************
import math
# Functions


def num_to_english(num, digit_place):
    """ Translates a number to english equiv
        Inputs:
            Num -  Number to be translated as integer
            Digit place - place (e.g tens = 2, hundreds = 3... etc) as integer
        """
    idx = num % 10  # gives you the whole number of the next place
    if idx > 2 and idx < 10 and digit_place == 1:  # Process twenty through ninety
        print(f"{numeral_names[idx]} {places[digit_place]}")
    else:  # otherwise, work on hundereds forward
        print(f"{numeral_names[idx]} {places[digit_place]} ")

    if num/10 > 1:  # We have more digits to process
        digit_place = digit_place + 1  # Process the next place
        # // is the operation that returns the whole number of a division
        num_to_english(num//10, digit_place)
    return("Done....")


# Initialize variables
ones_place = 0
# Dictionary of Names
numeral_names = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",  # ten,zero
    11: "Eleven",  # ten one
    12: "Twelve",  # ten two
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen"
}
tens_places = {
    0: "",
    1: "",
    2: "twenty",
    3: "thirty",
    4: "fourty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

places = {
    1: "",
    2: "tens",
    3: "hundred",
    4: "thousand",
    5: "hundred thousand",
    6: "million",
    7: "hundred million"
}
####
# Input the number to be translated
text_numeral = input("What is the amount of the check?")
# Convert it to Floating Point for later use
float_numeral = float(text_numeral)
# breaks up the floating part into whole part an decimal part
# Returns a tuple - multiple items in a single variable.

# More conversion so we can work with the numbers
whole_part = int(whole_part)
decimal_part = int(decimal_part)
print(f"You input: {float_numeral}")
print(f"Whole Number part is: {whole_part}")
print(f"Decimal part is: {decimal_part}")
# Is there a decimal portion of the number?
if decimal_part != 0:  # we found a decimal point
    num_to_english(decimal_part, 2)
    print("cents")

# Work with Tens and Ones Numbers

if whole_part > 0:
    # Get the name of the numeral from the dictionary
    if tens_and_ones > 0 and tens_and_ones < 20:  # between 1 and 19
        print(f"Translated: {numeral_names.get(tens_and_ones)} dollars")
        float_numeral = int(float_numeral/100)
        print(f'Float Numeral is now: {float_numeral}')
        # We have processed the tens and ones
    else:
        tens_flag = True  # we started processing at the tens portion
        num_to_english(float_numeral, 1)

# We now have a whole number where the tens and ones
# have been processed so we now work with Hundreds forward
if not (tens_flag):
    hundreds = float_numeral % 10
    if hundreds > 0:
        # for digit_number in range(1,len(str(hundreds))):
        num_to_english(float_numeral, 3)
