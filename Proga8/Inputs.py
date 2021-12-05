
class Inputs(object):

    def __init__(self, inputValues):
        self.inputValues = inputValues

    def validate(self):
        for inputValue in self.inputValues:
            inputValue.get_isValid()

    def enterValues(self):
        for inputValue in self.inputValues:
            inputValue.readValue()

    def get_isValid(self):
        errorMessages = ''
        for inputValue in self.inputValues:
            validationResult = inputValue.get_isValid()
            if validationResult is not True:
                errorMessages = errorMessages + validationResult
        if len(errorMessages) > 1:
            return errorMessages
        return True
