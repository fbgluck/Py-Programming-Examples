# This is a program that will translate a number into
# its English equivalent that can be used when writing
# a check
# *********************************************
import math
# Functions


def num_to_english(num, digit_place, result_string):
    """ Translates a number to english equiv
        Inputs:
            Num -  Number to be translated as integer
            Digit place - place (e.g tens = 2, hundreds = 3... etc) as integer
        """
# Modulus: % returns the remainder when the first operand is divided by the second
    idx = num % 10  # gives you the whole number of the next place
    if idx > 2 and idx < 10 and digit_place == 1:  # Process twenty through ninety
        result_string = numeral_names[idx] + \
            places[digit_place] + result_string
        # print(f"{numeral_names[idx]} {places[digit_place]}")
    else:  # otherwise, work on hundereds forward
        results_string = numeral_names[idx] + places[digit_place]

    if num/10 > 1:  # We have more digits to process
        digit_place = digit_place + 1  # Process the next place
        # // is the operation that returns the whole number of a division
        num_to_english(num//10, digit_place, result_string)
    return(result_string)


# Initialize variables
ones_place = 0
english_string = "cents"
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
decimal_part, whole_part = math.modf(float_numeral)
# More conversion so we can work with the numbers

whole_part = int(whole_part)
# decimal_part = int(decimal_part*100)
decimal_part = int(text_numeral[-2:])
print(f"You input: {float_numeral}")
print(f"Whole Number part is: {whole_part}")
print(f"Decimal part is: {decimal_part}")
# Is there a decimal portion of the number?
if decimal_part != 0:  # we found a decimal point
    print(num_to_english(decimal_part, 1, english_string))
# Work with Tens and Ones Numbers

if whole_part > 0:
    # Get the name of the numeral from the dictionary
    # if whole_part > 0 and whole_part < 20:  # between 1 and 19
    print({num_to_english(whole_part, 1, english_string)})
    print(" dollars")
    # else:
 #   num_to_english(float_numeral, 1)
