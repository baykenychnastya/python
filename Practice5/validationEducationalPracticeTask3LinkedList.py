
class Validation:

    @staticmethod
    def readInteger(inputMessage):
        data = input(inputMessage)

        try:
            data = int(data)
        except ValueError:
            print('The size must be represented by a positive number!')

        return data

    @staticmethod
    def readIntegerWithCheck(inputMessage, isValid, invalidInputMessage=None):
        data = input(inputMessage)
        try:
            data = int(data)
        except ValueError:
            print('The size must be represented by a positive number!')
            return Validation.readIntegerWithCheck(inputMessage, isValid, invalidInputMessage)

        if not isValid(data):
            print(invalidInputMessage)
            return Validation.readIntegerWithCheck(inputMessage, isValid, invalidInputMessage)

        return data
