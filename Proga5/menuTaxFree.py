from collectionTaxFree import TaxFreeCollection

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
                       '9 - save\n'
                       '10 - show states\n'
                       '0 - if you want to exit\n')

        if option == '1':
            collectionTaxFree.addNew()
            collectionTaxFree.saveChanges()
        elif option == '2':
            collectionTaxFree.sort()
            collectionTaxFree.saveChanges()
            collectionTaxFree.display()
        elif option == '3':
            collectionTaxFree.find()
        elif option == '4':
            collectionTaxFree.deleteByID()
            collectionTaxFree.saveChanges()
            collectionTaxFree.display()
        elif option == '5':
            collectionTaxFree.edit()
            collectionTaxFree.saveChanges()
            collectionTaxFree.display()
        elif option == '6':
            collectionTaxFree.display()
        elif option == '7':
            collectionTaxFree.caretaker.undo()
            collectionTaxFree.display()
        elif option == '8':
            collectionTaxFree.caretaker.redo()
            collectionTaxFree.display()
        elif option == '9':
            collectionTaxFree.caretaker.saveMemento()
        elif option == '10':
            collectionTaxFree.caretaker.show()
        elif option == '0':
            print('The program is finished...')
            exit()
        else:
            print('Please enter only the options offered in the menu!')
            menu()


menu()
