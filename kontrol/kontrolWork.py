from Input import Input, InputDate
from Inputs import Inputs
from validateVaccinationPointRequest import VALIDATION


class VaccinationPointRequest(object):

    def __init__(self, ID=None, Point=None, Time=None, Date=None, Name=None):
        self.ID = Input(ID, 'ID', [VALIDATION.validateInteger, VALIDATION.validatePositive])
        self.Point = Input(Point, 'Point', [VALIDATION.validateRequiredStringWithTrim])
        self.Time = Input(Time, 'Time', [VALIDATION.validateTimeString])
        self.Date = Input(Date, "Date", [VALIDATION.validateDateString])
        self.Name = Input(Name, 'Name', [lambda value: VALIDATION.patternValidation(value, '^[a-zA-Z]+$')])

        self.inputValues = Inputs([
            self.Point,
            self.Time,
            self.Date,
            self.Name])

    def toJson(self):
        return {
            "ID": self.ID.value,
            "Point": self.Point.value,
            "Time": self.Time.value,
            "Date": self.Date.value,
            "Name": self.Name.value
        }

    def display(self):
        print(self.toJson())
