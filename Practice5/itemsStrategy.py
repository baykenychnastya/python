from os.path import exists

from educationalPracticeTask3LinkedList import LinkedList, EnterFileName
from educationalPracticeTask3LinkedList_Generator import LinkedListGenerator
from validationEducationalPracticeTask3LinkedList import Validation

List = LinkedList()


class ConcreteStrategyGenerateUsingIterator():
    @staticmethod
    def getRangeElements():
        lowerPosition = Validation.readIntegerWithCheck('Enter the lower position of the range: ', lambda x: True)
        upperPosition = Validation.readIntegerWithCheck('Enter the upper position of the range: ',
                                                        lambda x: x > lowerPosition,
                                                        'The upper position must be greater than the lower!\n')
        return lowerPosition, upperPosition

    def generateData(self):
        count, lowerLimit, upperLimit = LinkedListGenerator.getGenerateParameters()

        generator = LinkedListGenerator.functionGenerator(lowerLimit, upperLimit)
        index = Validation.readInteger('Enter index: ')
        for i in range(count):
            List.insertPosition(next(generator), index)
            index += 1
        return List


class ConcreteStrategyGenerateUsingFile():

    def generateData(self):
        filename = EnterFileName()
        file_exists = exists(filename)
        if file_exists:
            f = open(filename)
            data = f.read()
            my_list = data.split(" ")
            index = Validation.readInteger('Enter index: ')
            for i in my_list:
                try:
                    i = int(i)
                    List.insertPosition(i, index)
                    index += 1
                except ValueError:
                    print(f'Element {i} is not integer')
        else:
            print('No file')
        return List
