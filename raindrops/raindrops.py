def has_three_as_factor(number):
    if (number % 3 == 0):
        return True
    else:
        return False

def has_five_as_factor(number):
    if (number % 5 == 0):
        return True
    else:
        return False

def has_seven_as_factor(number):
    if (number % 7 == 0):
        return True
    else:
        return False

def add_pling():
    return "Pling"

def add_plang():
    return "Plang"

def add_plong():
    return "Plong"


def convert(number):
    if(type(number) is not int):
        raise TypeError("Only integers allowed")
        return number
    sound_to_print = ""
    if has_three_as_factor(number):
        sound_to_print = "{}{}".format(sound_to_print, add_pling())
    if has_five_as_factor(number):
        sound_to_print = "{}{}".format(sound_to_print, add_plang())
    if has_seven_as_factor(number):
        sound_to_print = "{}{}".format(sound_to_print, add_plong())
    print(sound_to_print)
    if "" == sound_to_print:
        return "{}".format(number)
    else:
        return sound_to_print
