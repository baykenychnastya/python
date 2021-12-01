from VaccinationPointRequests import VaccinationPointRequests


def menu():
    v = VaccinationPointRequests()

    while True:
        option = input('Enter:\n1 - Add vaccination point\n'
                       '2 - Display vaccination points\n'
                       '3 - Most frequent time\n')

        if option == '1':
            v.addNew()
            v.saveChanges()
        elif option == '2':
            v.display()
        elif option == '3':
            v.mostFrequentTime()
        elif option == '0':
            print('The program is finished...')
            exit()
        else:
            print('Please enter only the options offered in the menu!')
            menu()


menu()

