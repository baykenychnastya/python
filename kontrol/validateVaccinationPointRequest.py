import re
import datetime


class VALIDATION:

    @staticmethod
    def validation_decorator(checkIsValid):
        def decorator(fun):
            def wrapper(*args, **kwargs):
                isValid = checkIsValid(args[1])

                if isValid is False:
                    return False
                fun(*args)
            return wrapper
        return decorator

    @staticmethod
    def validation_decorator_with_two_arguments(checkIsValid):
        def decorator(fun):
            def wrapper(*args, **kwargs):
                isValid = checkIsValid(args[1], args[2])

                if isValid is False:
                    return False
                fun(*args)
            return wrapper
        return decorator

    @staticmethod
    def patternValidation(value, regEx):
        pattern = re.compile(regEx)
        if pattern.match(value):
            return True

        print(f'Invalid value {value}: must match the regular expression {regEx}')
        return False

    @staticmethod
    def validateDateString(value):
        try:
            datetime.datetime.strptime(value, '%Y-%m-%d')
            return True
        except ValueError:
            print("Incorrect data format, must be YYYY-MM-DD")
            return False


    @staticmethod
    def validateTimeString(value):
        try:
            datetime.datetime.strptime(value, '%H:%M')
            return True
        except ValueError:
            print("Incorrect data format, must be HH:MM")
            return False

    @staticmethod
    def validateInteger(value):
        try:
            int(value)
            return True
        except ValueError:
            print(f'Value {value} must be integer')
            return False

    @staticmethod
    def validatePositive(value):
        if value < 0:
            print(f'Value {value} must be positive')
            return False

        return True

    @staticmethod
    def validateEnumValue(value, Enum):
        validValues = tuple(item.value for item in Enum)

        if value in validValues:
            return True

        print(f'Not valid value: {value}')
        return False

    @staticmethod
    def validateRequiredStringWithTrim(value):
        if len(value.strip()) > 0:
            return True

        print("Value is required")
        return False

    @staticmethod
    def validateLowerDateInputFile(value1, value2, invalidDataMessages):
        if value1.value <= value2:
            return True
        print(invalidDataMessages)
        return False

    @staticmethod
    def validateLowerDate(value1, value2, invalidDataMessages):
        if value1 <= value2:
            return True
        print(invalidDataMessages)
        return False

    @staticmethod
    def readInteger(inputMessage, invalidDataMessages):
        data = input(inputMessage)

        try:
            data = int(data)
        except ValueError:
            print(invalidDataMessages)
            return VALIDATION.readInteger(inputMessage, 'Value must be integer! ')

        return data

    @staticmethod
    def readIntegerWithCheck(inputMessage, isValid, invalidInputMessage=''):
        data = input(inputMessage)

        try:
            data = int(data)
        except ValueError:
            print('Data must be represented by a positive number!')
            return VALIDATION.readIntegerWithCheck(inputMessage, isValid, invalidInputMessage)

        if not isValid(data):
            print(invalidInputMessage)
            return VALIDATION.readIntegerWithCheck(inputMessage, isValid, invalidInputMessage)

        return data

    @staticmethod
    def validateName(inputMessage):
        data = input(inputMessage)

        try:
            data = str(data)
        except:
            print('Data must be represented by a positive number!')
            return VALIDATION.validateName(inputMessage)