def convert_number_to_list_of_digits(number):
    number_string = str(number)
    digits_as_string_list= list(number_string)
    digits_list = list(map(int, digits_as_string_list))
    return digits_list

def calculate_sum_of_digits_powers(list_of_digits):
    sum_of_digits_powers = 0
    for iterator in range(len(list_of_digits)):
        sum_of_digits_powers += list_of_digits[iterator]**len(list_of_digits)
    return sum_of_digits_powers

def is_armstrong_number(number):
    print(number)
    list_of_digits = convert_number_to_list_of_digits(number)
    print("{}".format(list_of_digits))
    sum_of_digits_powers = calculate_sum_of_digits_powers(list_of_digits)
    print("sum = {}".format(sum_of_digits_powers))
    if number == sum_of_digits_powers:
        return True
    else:
        return False
