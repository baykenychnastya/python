import re
import datetime


def patternValidation(value, regEx):
    pattern = re.compile(regEx)
    if pattern.match(value):
        return True

    print(f'Invalid value {value}: must match the regular expression {regEx}')
    return False


def validateDateString(value):
    try:
        datetime.datetime.strptime(value, '%Y-%m-%d')
        return True
    except ValueError:
        print("Incorrect data format, must be YYYY-MM-DD")
        return False


def validateInteger(value):
    try:
        int(value)
        return True
    except ValueError:
        print(f'Value {value} must be integer')
        return False


def validatePositive(value):
    if value < 0:
        print(f'Value {value} must be positive')
        return False

    return True


def validateEnumValue(value, Enum):
    validValues = tuple(item.value for item in Enum)

    if value in validValues:
        return True

    print(f'Not valid value: {value}')
    return False


def validateRequiredStringWithTrim(value):
    if len(value.strip()) > 0:
        return True

    print("Value is required")
    return False


def readInteger(inputMessage, invalidDataMessages):
    data = input(inputMessage)

    try:
        data = int(data)
    except ValueError:
        print(invalidDataMessages)
        return readInteger(inputMessage, invalidDataMessages)

    return data


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
