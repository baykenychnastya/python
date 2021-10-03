def readInteger(inputMessage):
    data = input(inputMessage)

    try:
        data = int(data)
    except ValueError:
        print('The size must be represented by a positive number!')

    return data


def readIntegerWithCheck(inputMessage, isValid, invalidInputMessage=''):
    data = input(inputMessage)

    try:
        data = int(data)
    except ValueError:
        print('The size must be represented by a positive number!')
        return readIntegerWithCheck(inputMessage, isValid, invalidInputMessage)

    if not isValid(data):
        print(invalidInputMessage)
        return readIntegerWithCheck(inputMessage, isValid, invalidInputMessage)

    return data
