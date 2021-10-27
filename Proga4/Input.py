from validationForTaxFree import *


class Input(object):

    def __init__(self, value, valueName, validations=[]):
        self.value = value
        self.validations = validations
        self.valueName = valueName

    def readValue(self):
        value = input(f'Enter {self.valueName}: ')
        isValid = self.validate(value)

        if isValid:
            self.value = value
            return

        self.readValue()

    def readValue2(self):
        value = input(f'Enter {self.valueName}: ')

        self.value = value
        return value

    def get_isValid(self):
        return self.validate(self.value)

    def validate(self, value):
        for validation in self.validations:
            if not validation(value):
                print(f'{self.valueName} is invalid')
                return False

        return True


class InputInteger(Input):

    def readValue(self):
        value = VALIDATION.readInteger(f'Enter {self.valueName}: ', 'Value must be integer')
        isValid = self.validate(value)

        if isValid:
            self.value = value
            return

        self.readValue()


class InputDate(Input):

    def readValue(self):
        print(f'Enter {self.valueName}: ')
        value = self.getDate()
        isValid = self.validate(str(value))

        if isValid:
            self.value = str(value)
            return

        self.readValue()

    def getDate(self):
        year = VALIDATION.readIntegerWithCheck('Enter year : ', lambda x: 0 < x < 2021, 'Invalid data, try again ')
        month = VALIDATION.readIntegerWithCheck('Enter month : ', lambda x: 0 < x < 13, 'Invalid data, try again ')
        day = VALIDATION.readIntegerWithCheck('Enter day : ', lambda x: 0 < x < 31, 'Invalid data, try again ')
        date = datetime.date(year, month, day)
        return date
