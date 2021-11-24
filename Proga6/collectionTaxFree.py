import itertools
import copy

from TaxFree import TAX_FREE
import json
from os.path import exists

from memento import Memento, Caretaker
from validationForTaxFree import VALIDATION


def enterFileName():
    print('Enter a file name: ')
    nameFile = 'js'
    nameFile += '.json'
    return nameFile


filename = enterFileName()


class TaxFreeCollection(object):
    taxFrees = []
    id_iter = None

    def __init__(self):
        file_exists = exists(filename)
        if file_exists:
            self.readDataFromFile()
        else:
            open(filename, 'a', encoding='utf-8')

        self.initIDIter()
        self.caretaker = Caretaker(self)
        self.caretaker.saveMemento()

    def readDataFromFile(self):
        taxFreesFromFile = []
        with open(filename, 'r', encoding='utf-8') as f:
            taxFreesJson = json.load(f)
        for taxFreeJson in taxFreesJson:
            taxFreesFromFile.append(TAX_FREE(**taxFreeJson))

        for index, taxFreeFromFile in enumerate(taxFreesFromFile):
            if taxFreeFromFile.checkIsValid():
                self.taxFrees.append(taxFreeFromFile)
            else:
                print(f'Above validation errors for tax free with index {index}')
                print()

    def initIDIter(self):
        if len(self.taxFrees) > 0:
            self.id_iter = itertools.count(start=self.taxFrees[-1].ID.value + 1)
        else:
            self.id_iter = itertools.count()

    def display(self):
        for obj in self.taxFrees:
            obj.display()

    def sort(self, attr):
        try:
            if attr == 'Company':
                self.taxFrees.sort(key=lambda x: str(getattr(x, f"get_{attr}")()).lower(), reverse=False)
            else:
                self.taxFrees.sort(key=lambda x: getattr(x, f"get_{attr}")(), reverse=False)
        except:
            print('Invalid data,try again ')
            self.sort()

    def generateID(self):
        id = next(self.id_iter)
        for TaxFree in self.taxFrees:
            if id == TaxFree.ID.value:
                return self.generateID()
        return id

    def addNew(self):
        tax = TAX_FREE()

        tax.ID.value = self.generateID()

        for method_name in dir(tax):
            if method_name.startswith("enter"):
                getattr(tax, method_name)()

        self.taxFrees.append(tax)

    def saveChanges(self):
        jsonCollection = json.dumps([obj.toJson() for obj in self.taxFrees], indent=2, default=str)

        with open(filename, 'w') as f:
            f.write(jsonCollection)

    def deleteByID(self, ID):
        for taxFree in self.taxFrees:
            if taxFree.ID.value == ID:
                self.taxFrees.remove(taxFree)
                return

    def edit(self):
        ID = VALIDATION.readInteger('Enter ID: ', 'Data must be represented by a positive number, try again ')
        self.editNoteByID(ID)

    def editNoteByID(self, ID):
        for taxFree in self.taxFrees:
            if taxFree.ID.value != ID:
                continue

            for method_name in dir(taxFree):
                if method_name.startswith("enter"):
                    getattr(taxFree, method_name)()
            return

    def find(self, data):
        print('Objects with coincidence:')

        for taxFree in self.taxFrees:
            for method_name in dir(taxFree):
                if method_name.startswith("get_") and str(f'{getattr(taxFree, method_name)()}').find(data) != -1:
                    return taxFree

        print('Unfortunately, there is no coincidence')
        return None

    def save(self):
        return Memento(copy.deepcopy(self.taxFrees))

    def load(self, state):
        self.taxFrees = state

    def __str__(self):
        return json.dumps([obj.toJson() for obj in self.taxFrees], indent=2, default=str)

    def __getitem__(self, index):
        if index >= len(self.taxFrees):
            return -1
        return self.taxFrees[index]

    def __len__(self):
        return len(self.taxFrees)

