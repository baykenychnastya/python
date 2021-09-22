#Розглянемо послідовності довжини N, що складаються з 0 і 1.
# Потрібно написати програму, яка за заданим натуральним числом N визначає кількість тих з них,
# в яких ніякі дві одиниці не стоять поруч.
#Вхідні дані:
#Число N (1 ≤ N ≤ 1000).

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

def getCountOfSequencesInWhichNoTwoDigitsOneStandSideBySide(N):
    result=int((2 ** N) - (((2 ** N) / 2) - 1))
    return result


N = readInteger('Enter length of the sequence:', 'Length of the sequence must be a number!')

if (N < 0):
    printMessageAndExit('The length of the sequence must be positive number!')
elif(N > 1000):
    printMessageAndExit('The length of the sequence must be less than a thousand!')
elif (N == 0):
    printMessageAndExit('The length of the sequence cannot be zero!')

print('The number of sequences in which no two 1 stand side by side: ', getCountOfSequencesInWhichNoTwoDigitsOneStandSideBySide(N))
