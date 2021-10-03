# Створити клас LinkedList, в якому повинні бути реалізовані наступні методи:
# Введення елементів з клавіатури
# Генерація елементів рандомно з проміжку [a,b]
# Додати елемент на k позицію
# Видалити елемент з k позиції
# Виконати метод, який зазначений у вашому варіанті
# Код повинен бути якісним, програма повинна бути поділена на файли.
# Змінити його наступним чином: спочатку виписати всі елементи з парними індексами,
# а потім із непарними (із збереженням їх відносного порядку).

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    length = 0

    def __init__(self):
        self.head = None
        self.last_node = None

    def insertElement(self, position, valueElement):
        self.length += 1
        if self.head is None:
            self.last_node = self.head = Node(valueElement)
            return
        if position == 0:
            self.head = Node(valueElement)
            return
        current = self.head
        count = 0
        while current is not None:
            count += 1
            if count == position:
                newNext = Node(current.data)
                newNext.next = current.next

                current.data = valueElement
                current.next = newNext

                if current.next.next is None:
                    self.last_node = current.next
                break
            current = current.next

    def deleteElement(self, position):
        self.length -= 1

        current = self.head
        previous = None
        count = 0

        while current is not None:
            count += 1
            if count == position:
                if previous is None:
                    self.head = current.next
                    break
                if current.next is None:
                    previous.next = None
                    break
                newNext = Node(current.next.data)
                newNext.next = current.next.next

                previous.next = newNext
                break

            previous = current
            current = current.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next

    def append(self, data):
        self.length += 1
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def getElementsWithEvenIndexes(self):
        elementsWithEvenIndexes = []
        count = 0

        current = self.head
        while current is not None:
            if count % 2 == 0 and count != 0:
                elementsWithEvenIndexes.append(current.data)

            count += 1
            current = current.next

        return elementsWithEvenIndexes

    def getElementsWithOddIndexes(self):
        oddIndexes = []
        count = 0

        current = self.head
        while current is not None:
            if count % 2 == 1 and count != 0:
                oddIndexes.append(current.data)

            count += 1
            current = current.next

        return oddIndexes
