# Write a function that converts a given currency number (in string format) into words. For example, if the input is "1234.25", the output should be "one thousand two hundred thirty-four dollars and twenty-five cents".
import math

location_to_unit_dict = {
    1: "thousand",
    2: "million",
    3: "billion",
    4: "trillion",
    5: "quadrillion",
}

number_to_word_dict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    0: "zero",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}
    
tens = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety",
}

def convert_3_digit_number_to_word(num):
    hundreds = num // 100
    tens_units = num % 100
    
    words = []
    
    if hundreds > 0:
        words.append(number_to_word_dict[hundreds])
        words.append("hundred")
    
    if tens_units > 0:
        if tens_units < 20:
            words.append(number_to_word_dict[tens_units])
        else:
            tens_place = tens_units // 10
            units_place = tens_units % 10
            
            words.append(tens[tens_place])
            if units_place > 0:
                words.append(number_to_word_dict[units_place])
    
    if words:
        return " ".join(words)
    else:
        return ""

def check_string_valid_number(number: str):
    try:
        float(number)
        return True
    except ValueError:
        print("Invalid number format. Please enter a valid currency number.")
        return False

def currency_to_word (input_number: str):
    if check_string_valid_number(input_number):
        whole_part = input_number.split(".")[0]
        max_unit = math.floor(len(whole_part)/3)
        result = ''
        for i in range(max_unit + 1):
            if i == max_unit:
                result += (convert_3_digit_number_to_word(int(whole_part[len(whole_part)%3 + i*3 -3:])) + ' ') if convert_3_digit_number_to_word(int(whole_part[len(whole_part)%3 + i*3 - 3:])) else ''
            elif i == 0:
                result += (convert_3_digit_number_to_word(int(whole_part[:len(whole_part)%3]))  + ' ' + location_to_unit_dict.get(max_unit - i, '') + ' ')
            else:
                result += (convert_3_digit_number_to_word(int(whole_part[len(whole_part)%3 + i*3 -3:len(whole_part)%3+3*i])) + ' ' + location_to_unit_dict.get(max_unit - i, '') + ' ')

        result += "dollars"
        if '.' in input_number:
            result += ' and '
            decimal_part = input_number.split(".")[1]
            result += convert_3_digit_number_to_word(int(decimal_part)) + ' cents'

        return result.strip()
    else:
        return "Invalid input. Please enter a valid currency number."

input_number = input("Put in a currency number with the following format: 1234.25 (one thousand two hundred thirty-four dollars and twenty-five cents): ")

result = currency_to_word(input_number=input_number)
print(result)