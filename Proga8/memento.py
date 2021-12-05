import copy
import json
from datetime import datetime


class Memento:
    def __init__(self, state):
        self.state = state

    def getState(self):
        return self.state

    def __str__(self):
        return json.dumps([obj.toJson() for obj in self.state], indent=2, default=str)


class Caretaker:
    def __init__(self, originator):
        self.originator = originator
        self.states = []
        self.statesPosition = -1

    def saveMemento(self):
        memento = self.originator.save()
        self.states.append(memento)
        self.statesPosition = len(self.states) - 1

    def undo(self):
        if len(self.states) == 0:
            return print("There are no saves")

        if self.statesPosition == 0:
            return print("There were no new changes")

        self.statesPosition -= 1
        memento = copy.deepcopy(self.states[self.statesPosition].getState())
        self.originator.load(memento)

    def redo(self):
        if len(self.states) == 0:
            return print("There are no saves")

        if len(self.states) - 1 == self.statesPosition:
            return print("There were no new changes")

        self.statesPosition += 1
        memento = copy.deepcopy(self.states[self.statesPosition].getState())
        self.originator.load(memento)
