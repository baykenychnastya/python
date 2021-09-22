# Користувач повинен мати 2 опції:
#ввести масив довжини N з клавіатури
#згенерувати довільний масив довжини N зі значень, які знаходяться в діапазоні [a, b], де a,b вводяться з клавіатури.
#Реалізувати алгоритм mergeSort для сортування даного масиву.
# Вивести кількість операцій, яка була необхідною для сортування масиву.
#Програма повинна закінчувати свою роботу тільки у випадку, коли користувач натиснув відповідний пункт меню.

operationsCount = 0

def readInteger(inputMessage, invalidDataMessages):
    data = input(inputMessage)

    try:
        data = int(data)
    except ValueError:
        print(invalidDataMessages)
        return readInteger(inputMessage, invalidDataMessages)

    return data

def inputArray():
    length = readInteger('Enter the length of the array:', 'The length must be represented by a number!')

    while length<1:
        print('The length must be represented by a positive number!')
        length = readInteger('Enter the length of the array:', 'The length must be represented by a number!')

    array = []

    for i in range(length):
        number = readInteger('Enter ' + str(i) + '-th element of array:', 'The date must be represented by a number!')
        array.append(number)
    return array

def checkIntervalIsValid(lowerLimit, upperLimit):
    return lowerLimit <= upperLimit

def generateArray():
    import random
    array = []
    size=readInteger('Enter the length of the array: ', 'The length must be represented by a number!')

    while size < 1:
        print('The length must be represented by a positive number!')
        size = readInteger('Enter the length of the array:', 'The length must be represented by a number!')

    lowerLimit=readInteger('Enter the lower limit of the range: ', 'The lower limit  must be represented by a number!')
    upperLimit=readInteger('Enter the upper limit of the range: ', 'The upper limit  must be represented by a number!')
    if checkIntervalIsValid(lowerLimit, upperLimit) is False:
        print('The upper limit must be greater than the lower!\n')
        return array
    for i in range(size):
        array.append(random.randint(lowerLimit, upperLimit))
    return array

import operator

def mergeSort(array, compare=operator.lt):
    global operationsCount
    if len(array) < 2:
        operationsCount += 1
        return array[:]
    else:
        middle = int(len(array) / 2)
        left = mergeSort(array[:middle], compare)
        right = mergeSort(array[middle:], compare)
        operationsCount += 1
        return merge(left, right, compare)

def merge(left, right, compare):
    global operationsCount

    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        operationsCount += 1
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        operationsCount += 1
        result.append(left[i])
        i += 1
    while j < len(right):
        operationsCount += 1
        result.append(right[j])
        j += 1
    return result

def createAndSortArray():
    mas = inputArray()
    print('Your array: ', mas)

    sortArray(mas)

def createAndSortGenerateArray():
    mas = generateArray()
    if mas == []:
        return

    print('Your array: ', mas)
    sortArray(mas)

def sortArray(mas):
    global operationsCount

    operationsCount = 0
    print('Sorted array by Merge Sort: ', mergeSort(mas))
    print('Number of operations = ', operationsCount)

while True:
    mas = []
    choose = input('Press 1 if you want to enter an array of length N from the keyboard \nPress 2 if you want to generate an arbitrary array of length N \nPress 3 to exit the program: ')
    operationsCount = 0
    if choose == '1':
        createAndSortArray()
    elif choose == '2':
        createAndSortGenerateArray()
    elif choose == '3':
        break
    else:
        print('Please enter only the options offered in the menu!\n')
print('The program is finished...')
