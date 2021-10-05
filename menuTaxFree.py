from collectionTaxFree import TaxFreeCollection




collectionTaxFree = TaxFreeCollection()
collectionTaxFree.display()

option = input('Enter:\n 1 - if you want to search\n'
               '2 - if you want to sort\n'
               '3 - if you want to delete the note by ID\n'
               '4 - if you want to add note to the file\n'
               '5 - if you want to edit note by ID'
               '6 - if you want to exit\n ')

if option == '1':
    data = input('Enter something:')
    collectionTaxFree.find(data)
elif option == '2':
    collectionTaxFree.sort()
    collectionTaxFree.display()
elif option == '3':
    ID = int(input('Enter ID: '))
    collectionTaxFree.deleteByID(ID)
    collectionTaxFree.saveChanges()
    collectionTaxFree.display()
elif option == '4':
    collectionTaxFree.addNew()
    collectionTaxFree.saveChanges()
elif option == '5':
    ID = int(input('Enter ID: '))
    collectionTaxFree.editNoteByID(ID)
    collectionTaxFree.display()
elif option == '6':
    print('The program is finished...')
    exit()
