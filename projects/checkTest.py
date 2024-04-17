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
    "0": "",
    "1": "",
    "2": "twenty",
    "3": "thirty",
    "4": "fourty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety"
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
def translate(index,maxDigits, numericalAmount):
    resultString=""
    if index == 1:
        if int(numericalAmount) <=19:
            resultString = numeral_names[numericalAmount] + resultString
        else:
            resultString= tens_places[numericalAmount[-2]]+ " "
            resultString= resultString + numeral_names["0" + numericalAmount[-1]]
    resultString = "and " + resultString + " cents"
    return(resultString)

## --- Main Program Begins Here ----
checkAmount = input("Amount of check (nn.nn format): >> ")

amountLength = len(checkAmount) # set to the length of the string entered

print (f"Length of amount is: {amountLength}")
for i in range(-1,-4,-1):
    print(f"Place: {i}, value:{checkAmount[i]}")

print (f"Calling translate  with {checkAmount[-2:2]}")
textResult =  translate(i, amountLength, checkAmount[-2:2]) #- Call the subrouting translation
print(textResult)
    
