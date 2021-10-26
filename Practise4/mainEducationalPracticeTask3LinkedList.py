from educationalPracticeTask3LinkedList_Generator import *
from educationalPracticeTask3LinkedList import LinkedList
from validationEducationalPracticeTask3LinkedList import Validation
import random


def createList():
    List = LinkedList()
    count = Validation.readIntegerWithCheck('How many elements would you like to add? ', lambda x: x > 0,
                                            'The length must be represented by a positive number!')
    for i in range(count):
        data = Validation.readIntegerWithCheck('Enter ' + str(i + 1) + '-th element of list:', lambda x: True,
                                               'Invalid data')
        List.append(data)
    return List


def generateList():
    count, lowerLimit, upperLimit = LinkedListGenerator.getGenerateParameters()

    List = LinkedList()

    for i in range(count):
        List.append(random.randint(lowerLimit, upperLimit))
    return List


def createListWithMenu():
    option = input('Enter:\n1 - to enter list items from the keyboard\n'
                   '2 - generate elements randomly from a to b\n')

    if option == '1':
        return createList()

    elif option == '2':
        option1 = input('Enter:\n1 - generate elements randomly from a to b\n'
                        '2 - generate elements randomly from a to b using function generator\n')
        if option1 == '1':
            return generateList()
        if option1 == '2':
            Generator = LinkedListGenerator.GenerateListUsingGenerator()
            for node in Generator:
                print(node.data)

            return Generator
    else:
        print('Please enter only the options offered in the menu!\n')
        return createListWithMenu()


def manipulateListWithMenu(List):
    while True:
        option = input('Enter:\n1 - Add an element to the k position\n'
                       '2 - Remove the item from the k position\n'
                       '3 - first write all the elements with even indices,and then with odd\n'
                       '4 - if you want to finished ')
        if option == '1':
            position = Validation.readIntegerWithCheck('Enter a position: ', lambda x: 0 < x <= List.length,
                                                       'Invalid data, try again ')
            element = Validation.readInteger('Enter the items you want to add: ')
            List.insertElement(position, element)
            List.display()

        elif option == '2':
            position = Validation.readIntegerWithCheck('Enter a position: ', lambda x: 0 < x <= List.length,
                                                       'Invalid data, try again ')
            List.deleteElement(position)
            List.display()

        elif option == '3':
            result = List.getElementsWithEvenIndexes() + List.getElementsWithOddIndexes()
            print(*result, sep=", ")

        elif option == '4':
            print('Program is finished. . .')
            exit()
        else:
            print('Please enter only the options offered in the menu!')
            manipulateListWithMenu(List)


List = createListWithMenu()
List.display()
manipulateListWithMenu(List)
