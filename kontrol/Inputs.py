
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
        return all([inputValue.get_isValid() for inputValue in self.inputValues])
