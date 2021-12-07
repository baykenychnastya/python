from collectionTaxFree import TaxFreeCollection
from validationForTaxFree import VALIDATION

collectionTaxFree = TaxFreeCollection()


def menu():
    while True:
        option = input('Enter:\n1 -  if you want to add note to the file\n'
                       '2 - if you want to sort\n'
                       '3 - if you want to search\n'
                       '4 - if you want to delete the note by ID\n'
                       '5 - if you want to edit note by ID\n'
                       '6 - if you want to see the entire contents of the file\n'
                       '7 - undo\n'
                       '8 - redo\n'
                       '0 - if you want to exit\n')

        if option == '1':
            collectionTaxFree.addNew()
            collectionTaxFree.saveChanges()
            collectionTaxFree.caretaker.saveMemento()
            collectionTaxFree.display()
        elif option == '2':
            print("Attribute for sort:")
            attr = input()
            collectionTaxFree.sort(attr)
            collectionTaxFree.saveChanges()
            collectionTaxFree.caretaker.saveMemento()
            collectionTaxFree.display()
        elif option == '3':
            print('Enter something:')
            data = input()
            obj = collectionTaxFree.find(data)
            if obj is not None:
                obj.display()
        elif option == '4':
            ID = VALIDATION.readInteger('Enter ID: ', 'Data must be represented by a positive number, try again ')
            collectionTaxFree.deleteByID(ID)
            collectionTaxFree.saveChanges()
            collectionTaxFree.caretaker.saveMemento()
            collectionTaxFree.display()
        elif option == '5':
            collectionTaxFree.edit()
            collectionTaxFree.saveChanges()
            collectionTaxFree.caretaker.saveMemento()
            collectionTaxFree.display()
        elif option == '6':
            collectionTaxFree.display()
        elif option == '7':
            collectionTaxFree.caretaker.undo()
            collectionTaxFree.saveChanges()
            collectionTaxFree.display()
        elif option == '8':
            collectionTaxFree.caretaker.redo()
            collectionTaxFree.saveChanges()
            collectionTaxFree.display()
        elif option == '0':
            print('The program is finished...')
            exit()
        else:
            print('Please enter only the options offered in the menu!')
            menu()


menu()
