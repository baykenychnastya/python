from educationalPracticeTask3LinkedList import LinkedList
from educationalPracticeTask3LinkedList_Generator import LinkedListGenerator
from itemsStrategy import ConcreteStrategyGenerateUsingFile, ConcreteStrategyGenerateUsingIterator
from validationEducationalPracticeTask3LinkedList import Validation


def menu():
    List = LinkedList()
    strategy = None

    while True:
        option = input('\n\n\nEnter:\n1 - Use strategy 1 to insert into the list(Generate using an iterator)\n'
                       '2 - Use strategy 2 to insert into the list(Read data from a file)\n'
                       '3 - Generate data\n'
                       '4 - Delete the item at the specified position\n'
                       '5 - Delete multiple items within the start and end positions\n'
                       '6 - First write all the elements with even indices,and then with odd\n'
                       '7 - Display a list\n'
                       '8 - If you want to exit\n'
                       '0 - if you want to save changes to the file\n')
        if option == '0':
            List.saveChanges()
        if option == '1':
            print('You have chosen strategy №1(Generate using an iterator)')
            strategy = ConcreteStrategyGenerateUsingIterator()
        elif option == '2':
            print('You have chosen strategy №2(Read data from a file)')
            strategy = ConcreteStrategyGenerateUsingFile()
        elif option == '3':
            if strategy is None:
                print('Please, select strategy')
                menu()
            List = strategy.generateData()
        elif option == '4':
            position = Validation.readIntegerWithCheck('Enter a position: ', lambda x: 0 < x <= List.length,
                                                       'Invalid data, try again ')
            List.deleteElement(position)
            List.display()
        elif option == '5':
            lowerPosition, upperPosition = LinkedListGenerator.getRangeElements()
            List.deleteRangeElements(lowerPosition, upperPosition)
        elif option == '6':
            result = List.getElementsWithEvenIndexes() + List.getElementsWithOddIndexes()
            print(*result, sep=", ")
            List = LinkedList()
            for i in result:
                List.append(i)
        elif option == '7':
            print('Your current list')
            List.display()
        elif option == '8':
            print('The program is finished...')
            exit()
        else:
            print('Please enter only the options offered in the menu!')
            menu()


menu()
