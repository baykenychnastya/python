from educationalPracticeTask3LinkedList import LinkedList
from validationEducationalPracticeTask3LinkedList import readInteger
from validationEducationalPracticeTask3LinkedList import readIntegerWithCheck


def createList():
    List = LinkedList()
    count = readIntegerWithCheck('How many elements would you like to add? ', lambda x: x > 0,
                                 'The length must be represented by a positive number!')
    for i in range(count):
        data = readIntegerWithCheck('Enter ' + str(i + 1) + '-th element of list:', lambda x: True, 'Invalid data')
        List.append(data)
    return List


def generateList():
    import random

    List = LinkedList()

    count = readIntegerWithCheck('How many elements would you like to add? ', lambda x: x > 0,
                                 'The length must be represented by a positive number!')

    lowerLimit = readIntegerWithCheck('Enter the lower limit of the range: ', lambda x: True)
    upperLimit = readIntegerWithCheck('Enter the upper limit of the range: ', lambda x: x > lowerLimit, 'The upper limit must be greater than the lower!\n')

    for i in range(count):
        List.append(random.randint(lowerLimit, upperLimit))
    return List


def createListWithMenu():
    option = input('Enter:\n1 - to enter list items from the keyboard\n2 - generate elements randomly from a to b\n')

    if option == '1':
        return createList()

    elif option == '2':
        return generateList()

    else:
        print('Please enter only the options offered in the menu!\n')
        return createListWithMenu()


def manipulateListWithMenu(List):
    while True:
        option = input('Enter:\n1 - Add an element to the k position\n2 - Remove the item from the k position\n'
                       '3 - first write all the elements with even indices,and then with odd\n4 - if you want to finished ')
        if option == '1':
            position = readIntegerWithCheck('Enter a position: ', lambda x: 0 < x <= List.length,
                                            'Invalid data, try again ')
            element = readInteger('Enter the items you want to add: ')
            List.insertElement(position, element)
            List.display()

        elif option == '2':
            position = readIntegerWithCheck('Enter a position: ', lambda x: 0 < x <= List.length,
                                            'Invalid data, try again ')
            List.deleteElement(position)
            List.display()

        elif option == '3':
            result = List.getElementsWithEvenIndexes() + List.getElementsWithOddIndexes()
            print(*result, sep=", ")

        elif option == '4':
            print('Program is finished. . .')
            break
        else:
            print('Please enter only the options offered in the menu!')
            manipulateListWithMenu(List)


List = createListWithMenu()
List.display()
manipulateListWithMenu(List)
