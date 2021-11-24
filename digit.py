dictionary = {
    'Black': {
        'digit': 0,
        'multiplier': 1,
        'tolerance': None,
        'temperature': 250
    },
    'Brown': {
        'digit': 1,
        'multiplier': 10,
        'tolerance': 1,
        'temperature': 100
    },
    'Red': {
        'digit': 2,
        'multiplier': 100,
        'tolerance': 2,
        'temperature': 50
    },
    'Orange': {
        'digit': 3,
        'multiplier': 1000,
        'tolerance': None,
        'temperature': 15
    },
    'Yellow': {
        'digit': 4,
        'multiplier': 10000,
        'tolerance': None,
        'temperature': 25
    },
    'Green': {
        'digit': 5,
        'multiplier': 100000,
        'tolerance': 0.5,
        'temperature': 20
    },
    'Blue': {
        'digit': 6,
        'multiplier': 1000000,
        'tolerance': 0.25,
        'temperature': 10
    },
    'Violet': {
        'digit': 7,
        'multiplier': None,
        'tolerance': 0.1,
        'temperature': 5
    },
    'Grey': {
        'digit': 8,
        'multiplier': None,
        'tolerance': None,
        'temperature': 1
    },
    'White': {
        'digit': 9,
        'multiplier': None,
        'tolerance': None,
        'temperature': None
    },
    'Gold': {
        'digit': None,
        'multiplier': 0.1,
        'tolerance': 5,
        'temperature': None
    },
    'Silver': {
        'digit': None,
        'multiplier': 0.01,
        'tolerance': 10,
        'temperature': None
    },
}

def sorte(digits):
    for x, y in dictionary.items():
        if digits[0] == x:
            temp1 = y['digit']
        if digits[0] != x:
            temp1 = 0

        if digits[1] == x:
            temp2 = y['digit']
        if digits[1] != x:
            temp2 = 0

        if digits[2] == x:
            temp3 = y['digit']

        if digits[3] == x:
            temp4 = y['multiplier']

        if digits[4] == x:
            temp5 = y['tolerance']

    return [temp1, temp2, temp3, temp4, temp5]
