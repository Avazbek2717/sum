
d = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
            }

def romnan_int(roman_number: str) ->int:
    result = 0
    for i in roman_number:
        result += d[i]

    return result

print(romnan_int('M'))
