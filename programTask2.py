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


while True:
    print('To exit the program, press 0')

    length = readPositivInteger('Enter the dimension of the matrix:', 'The dimension must be represented by a positive number!')

    if length == -1:
        continue
    elif length == 0:
        break

    mat = [[0]*length for i in range(length)]

    for i in range(length):
        mat[i][i]=(i+1)*(i+2)

    print('The matrix is formed: ')
    printMatrix(mat)

print('The program is finished...')