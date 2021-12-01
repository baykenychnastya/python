import itertools
import json
from os.path import exists

from kontrolWork import VaccinationPointRequest


def enterFileName():
    print('Enter a file name: ')
    nameFile = input()
    nameFile += '.json'
    return nameFile


class VaccinationPointRequests(object):
    vaccinationPoints = []
    id_iter = None

    def __init__(self):
        self.filename = enterFileName()
        file_exists = exists(self.filename)
        if file_exists:
            self.readDataFromFile()
        else:
            open(self.filename, 'a', encoding='utf-8')

        self.initIDIter()

    def readDataFromFile(self):
        vaccinationPointsFromFile = []
        with open(self.filename, 'r', encoding='utf-8') as f:
            vaccinationPointsJson = json.load(f)
        for vaccinationPointJson in vaccinationPointsJson:
            vaccinationPointsFromFile.append(VaccinationPointRequest(**vaccinationPointJson))

        for index, vaccinationPointFromFile in enumerate(vaccinationPointsFromFile):
            self.vaccinationPoints.append(vaccinationPointFromFile)
            # if vaccinationPointFromFile.checkIsValid():
            #     self.vaccinationPoints.append(vaccinationPointFromFile)
            # else:
            #     print(f'Above validation errors for vaccination point with index {index}')
            #     print()

    def initIDIter(self):
        if len(self.vaccinationPoints) > 0:
            self.id_iter = itertools.count(start=self.vaccinationPoints[-1].ID.value + 1)
        else:
            self.id_iter = itertools.count()

    def display(self):
        for obj in self.vaccinationPoints:
            obj.display()

    def generateID(self):
        id = next(self.id_iter)
        for vaccinationPoint in self.vaccinationPoints:
            if id == vaccinationPoint.ID.value:
                return self.generateID()
        return id

    def addNew(self):
        point = VaccinationPointRequest()

        point.ID.value = self.generateID()
        point.inputValues.enterValues()

        if self.validateVaccinationPoint(point):
            self.vaccinationPoints.append(point)

    def mostFrequentTime(self):
        counter = 0
        num = [self.vaccinationPoints[0]]

        for i in self.vaccinationPoints:
            curr_frequency = len(list(filter(lambda v: v.Time.value == i.Time.value, self.vaccinationPoints)))

            if curr_frequency == counter:
                num.append(i)
            if curr_frequency > counter:
                counter = curr_frequency
                num = [i]

        uniqList = {x.Time.value: x for x in num}.values()
        for i in uniqList:
            print(i.Time.value)


    def validateVaccinationPoint(self, vaccinationPoint):
        isPointForNameArranged =\
            len(list(filter(lambda v: v.Name.value == vaccinationPoint.Name.value, self.vaccinationPoints))) > 0

        if isPointForNameArranged:
            print(f'Person with name: {vaccinationPoint.Name.value} is already registered for vaccination')
            return False

        count = len(
            list(filter(lambda v: v.Point.value == vaccinationPoint.Point.value and
                                  v.Time.value == vaccinationPoint.Time.value and
                                v.Date.value == vaccinationPoint.Date.value,
            self.vaccinationPoints)))

        if count >= 20:
            print("No places available. Please select different place or time!!!")
            return False

        return True



    def saveChanges(self):
        jsonCollection = json.dumps([obj.toJson() for obj in self.vaccinationPoints], indent=2, default=str)

        with open(self.filename, 'w') as f:
            f.write(jsonCollection)

    def __str__(self):
        return json.dumps([obj.toJson() for obj in self.vaccinationPoints], indent=2, default=str)
