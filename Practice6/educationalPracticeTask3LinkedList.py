from educationalPractice_observer import Event, Observer, Change


def EnterFileName():
    print('Enter the file name where you want to insert the data: ')
    nameFile = input()
    nameFile += '.txt'
    return nameFile

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    length = 0

    def __init__(self):
        self.head = None
        self.last_node = None
        self.current = None

        self.event = Event()
        self.event.signUp(Observer())

    def __str__(self):
        data = []
        for item in self:
            data.append(item.data)
        return str(data)

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

    def __len__(self):
        return self.length

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
            count += 1
            previous = current
            current = current.next


    def deleteRangeElements(self, lowerPosition, upperPosition):
        if lowerPosition > upperPosition:
            lowerPosition, upperPosition = upperPosition, lowerPosition

        count = upperPosition - lowerPosition + 1

        for i in range(count):
            self.deleteElement(lowerPosition)

    def getChange(self, data):
        self.head = Node(data, self.head)
        self.length += 1

    def insertPosition(self, data, index):
        if index > self.length:
            return print(f"Cannot insert into index  {index}")

        if index == 0:
            self.getChange(data)
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = Node(data, current.next)
            self.length += 1

        return 1

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

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next

    def saveChanges(self):
        filename = EnterFileName()
        current = self.head

        res = ''
        while current is not None:
            res += f' {current.data}'
            current = current.next

        with open(filename, "w") as somefile:
            somefile.write(res)

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

    def removeEvent(self, index, listBeforeChanges):
        listAfterChanges = str(self)

        self.event.trigger(
            Change(
                "remove", {
                    "event": "remove",
                    "listBeforeChanges": listBeforeChanges,
                    "positionOfRemove": index,
                    "listAfterChanges": listAfterChanges
                }))

    def addEvent(self, index, listBeforeChanges):
        listAfterChanges = str(self)

        self.event.trigger(
            Change(
                "add", {
                    "event": "add",
                    "listBeforeChanges": listBeforeChanges,
                    "positionOfInsert": index,
                    "listAfterChanges": listAfterChanges
                }))

    def removeRangEvent(self, a, b, listBeforeChanges):
        listAfterChanges = str(self)
        self.event.trigger(
            Change(
                "remove", {
                    "event": "remove range",
                    "listBeforeChanges": listBeforeChanges,
                    "rangOfRemove": [a, b],
                    "listAfterChanges": listAfterChanges
                }))
