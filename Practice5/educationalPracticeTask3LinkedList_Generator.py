from validationEducationalPracticeTask3LinkedList import Validation
import random


class LinkedListGenerator:
    @staticmethod
    def getRangeElements():
        lowerPosition = Validation.readIntegerWithCheck('Enter the lower position of the range: ', lambda x: True)
        upperPosition = Validation.readIntegerWithCheck('Enter the upper position of the range: ',
                                                        lambda x: x >= lowerPosition,
                                                        'The upper position must be greater than the lower!\n')
        return lowerPosition, upperPosition

    @staticmethod
    def getGenerateParameters():
        count = Validation.readIntegerWithCheck('How many elements would you like to add? ', lambda x: x > 0,
                                                'The length must be represented by a positive number!')

        lowerLimit = Validation.readIntegerWithCheck('Enter the lower limit of the range: ', lambda x: True)
        upperLimit = Validation.readIntegerWithCheck('Enter the upper limit of the range: ', lambda x: x > lowerLimit,
                                                     'The upper limit must be greater than the lower!\n')
        return count, lowerLimit, upperLimit

    @staticmethod
    def functionGenerator(lowerLimit, upperLimit):
        while True:
            yield random.randint(lowerLimit, upperLimit)

"""    @staticmethod
    def GenerateListUsingGenerator():
        count, lowerLimit, upperLimit = LinkedListGenerator.getGenerateParameters()

        List = LinkedList()

        generator = LinkedListGenerator.functionGenerator(lowerLimit, upperLimit)

        for i in range(count):
            List.append(next(generator))
        return List"""


