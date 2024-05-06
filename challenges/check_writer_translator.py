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
    if idx >= 1 and idx <= 9 and digit_place == 1:  # Process twenty through ninety
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
english_string = " cents"
# Dictionary of Names
numeral_names = {
    "00": "zero",
    "01": "one",
    "02": "two",
    "03": "three",
    "04": "four",
    "05": "five",
    "06": "six",
    "07": "seven",
    "08": "eight",
    "09": "nine",
    "10": "ten",  # ten,zero
    "11": "Eleven",  # ten one
    "12": "Twelve",  # ten two
    "13": "Thirteen",
    "14": "Fourteen",
    "15": "Fifteen",
    "16": "Sixteen",
    "17": "Seventeen",
    "18": "Eighteen",
    "19": "Nineteen"

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
print (f"You entered - {text_numeral}")
# Check to see if string has a decimal point
decimal_location = text_numeral.find(".")
if decimal_location < 0:
    print(f"ERROR - You input {text_numeral}. This number must contain a decimal point")
# Check to see that decimal point has only two characters following it
if text_numeral[-3] != ".":
    print(f"ERROR - Only two numbers can follow the decimal point")

# Split string at the decimal point into two parts
# whole part:
# decimal part:
splitString = text_numeral.split(".")
whole_part=splitString[0]
decimal_part=splitString[1]
# Check that both parts have only numerical values
if not(whole_part.isnumeric()):
    print(f'Whole part of your entry {whole_part} can only be numeric')
if not(decimal_part.isnumeric()):
    print(f'Decimal part of your entry {decimal_part} can only be numeric')
