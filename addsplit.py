import re

def is_first_dec(string):
    pattern_start_with_decimal = re.compile("[\d]+[\w/]*") # 123 | 123A | 1AB
    if re.match(pattern_start_with_decimal, string):
        return True
    else:
        return False

def is_house_format(string):
    pattern_house = re.compile("[\d]+[-/ ]*[\w]*") # 123 b | 123-b | 123-125 | 123/b
    if re.match(pattern_house, string):
        return True
    else:
        return False

def contains_street(string):
    pattern_street = re.compile("(str)|(av)|(rue)|(calle)|(weg)|(lein)", re.IGNORECASE) # having identificators
    if re.search(pattern_street, string):
        return True
    else:
        return False

def address_split(address):
    pattern_split = re.compile("[,\s]*", re.UNICODE) # whitespace elements && , +
    pattern_number = re.compile("(No)|(Num[bm]er)|(Num)|(Nr)")

    line = address.strip()
    # splitting by 1st ", " if exists
    if (re.search(", ", line)):
        array = line.split(", ", 1)
        if contains_street(array[0]) or not re.search("\d+", array[0]):
            street = array[0]
            house = array[1]
            return street, house
        else:
            street = array[1]
            house = array[0]
            return street, house

    array = pattern_split.split(line)

    if len(array) < 2:
        raise ValueError("Empty line or just one argument!")
    elif len(array) == 2:
        street = str(array[0])
        house = str(array[1])
        return street, house
    else: # len >2, assuming there is no input with len <2
        if not is_house_format(array[-1]): #if the last elements doesn't match house number pattern
            if is_first_dec(array[-2]):    #if previous starts with decimal, e.g. "24 A"
                street = " ".join(array[:-2])
                house = " ".join(array[-2:])
                return street, house
            else:   #both text elements -> assuming that number goes first
                house = str(array[0])
                street = " ".join(array[1:])
                return street, house
        else:
            if re.match(pattern_number, array[-2]): # e.g. "No 127"
                street = " ".join(array[:-2])
                house = " ".join(array[-2:])
                return street, house
            else:   # number is on the last place
                street = " ".join(array[:-1])
                house = str(array[-1])
                return street, house
