#Create a function taking a positive integer between 1 and 3999 (both included) as its parameter and returning a string containing the Roman Numeral representation of that integer.

#Modern Roman numerals are written by expressing each digit separately starting with the leftmost digit and skipping any digit with a value of zero. There cannot be more than 3 identical symbols in a row.

#In Roman numerals:

#1990 is rendered: 1000=M + 900=CM + 90=XC; resulting in MCMXC.
#2008 is written as 2000=MM, 8=VIII; or MMVIII.
#1666 uses each Roman symbol in descending order: MDCLXVI.
#Example:

#   1 -->       "I"
#1000 -->       "M"
#1666 --> "MDCLXVI"
#Help:

#Symbol    Value
#I          1
#V          5
#X          10
#L          50
#C          100
#D          500
#M          1,000

def solution(number):
    long_form = []
    for i, digit in enumerate(str(number)[::-1]):
        if int(digit) != 0:
            long_form.append(int(digit) * 10 ** i)
    
    roman = ""
    for p in reversed(long_form):
        if p > 999:
            roman += (p//1000)*"M"
        if p > 99:
            if p >= 100 and p <= 300:
                roman += (p//100)*"C"
            elif p == 400:
                roman += "CD"
            elif p == 500:
                roman += "D"
            elif p >= 600 and p <= 800:
                roman += "D"
                roman += ((p//100) - 5)*"C"
            elif p >= 900 and p < 1000:
                roman += "CM"
        if p > 9 and p < 100:
            if p >= 10 and p <= 30:
                roman += (p//10) * "X"
            elif p == 40:
                roman += "XL"
            elif p == 50:
                roman += "L"
            elif p >= 60 and p <= 80:
                roman += "L"
                roman += ((p//10) - 5) * "X"
            elif p == 90:
                roman += "XC"
        if p < 10 and p > 0:
            if p >= 1 and p <= 3:
                roman += (p//1) * "I"
            elif p == 4:
                roman += "IV"
            elif p == 5:
                roman += "V"
            elif p >= 6 and p <= 8:
                roman += "V"
                roman += ((p//1) - 5) * "I"
            elif p == 9:
                roman += "IX"
    return roman
