class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    length = 0

    def __init__(self):
        self.head = None
        self.last_node = None
        self.current = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.head is None:
            raise StopIteration

        if self.current is None:
            self.current = self.head
            return self.current
        self.current = self.current.next

        if self.current is not None:
            return self.current

        self.current = None
        raise StopIteration

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
        for node in self:
            print(node.data, end=' ')

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
