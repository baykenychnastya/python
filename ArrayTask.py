#Задано масив цілих чисел розмірності n.
# Змінити його наступним чином: спочатку виписати всі елементи з парними індексами,
# а потім із непарними (із збереженням їх відносного порядку).
def printMessageAndExit(message):
    print(message)
    exit()

def readInteger(inputMessage, invalidDataMessages):
    data = input(inputMessage)

    try:
        data = int(data)
    except ValueError:
        printMessageAndExit(invalidDataMessages)

    return data


def getElementsWithEvenIndexes(array):
    elementsWithEvenIndexes = []
    count = 0

    for i in array:
        if count % 2 == 0 and count != 0:
             elementsWithEvenIndexes.append(i)

        count += 1

    return  elementsWithEvenIndexes

def getElementsWithOddIndexes(array):
    oddIndexes = []
    count = 0

    for i in array:
        if count % 2 == 1:
            oddIndexes.append(i)

        count += 1

    return oddIndexes




length = readInteger('Enter a size:', 'The size must be represented by a number!')

if length<1:
    printMessageAndExit('The size must be represented by a positive number!')

array = []

for i in range(length):
    array.append(readInteger('Enter ' + str(i) + '-th element of array:', 'The date must be represented by a number!'))

result=getElementsWithEvenIndexes(array)+getElementsWithOddIndexes(array)

print('Elements with even indices and then with odd ones:', result)
