
def readIntegerWithCheck(inputMessage, isValid, invalidInputMessage=''):
    data = input(inputMessage)

    try:
        data = int(data)
    except ValueError:
        print('Data must be represented by a positive number!')
        return readIntegerWithCheck(inputMessage, isValid, invalidInputMessage)

    if not isValid(data):
        print(invalidInputMessage)
        return readIntegerWithCheck(inputMessage, isValid, invalidInputMessage)

    return data


"""def readDay(inputMessage, invalidDataMessages):
    data = input(inputMessage)
    
    try:
        data = int(data)
    except ValueError:
        print(invalidDataMessages)
    if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
        data < 31
    elif month ==
"""

def checkVadCoode(inputMessage):
    data = input(inputMessage)
    import re
    pattern = re.compile("^VA.{3,3}_.{2,2}_.{3,3}$")
    if pattern.match(data):
        return data
    else:
        print('Invalid data: ')
        return checkVadCoode(inputMessage)
