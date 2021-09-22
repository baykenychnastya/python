#Утворити квадратну матрицю порядку n і вивести її на екран


def readPositivInteger(inputMessage, invalidDataMessages):
    data = input(inputMessage)

    try:
        data = int(data)
    except ValueError:
        print(invalidDataMessages)
        return -1

    if data<0:
        print(invalidDataMessages)
        return -1

    return data

def printMatrix ( mat ):
   for row in mat:
      for x in row:
          print ( "{:4d}".format(x), end = "" )
      print ()

def generateMatrix(sizeMatrix):
    mat = [[0] * sizeMatrix for i in range(sizeMatrix)]

    for i in range(sizeMatrix):
        mat[i][i] = (i + 1) * (i + 2)
    return mat


while True:
    print("To exit the program, press 0")
    sizeMatrix = readPositivInteger('Enter the dimension of the matrix:','The dimension must be represented by a positive number!')

    if sizeMatrix == -1:
        continue
    elif sizeMatrix == 0:
        break
    print('The matrix is formed: ')
    printMatrix(generateMatrix(sizeMatrix))

print('The program is finished...')
