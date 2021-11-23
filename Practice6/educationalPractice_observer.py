import sys
import json

from educationalPractice_logger import Logger


class Change():
    def __init__(self, title, options):
        self.name = title
        self.options = options

    def __str__(self) -> str:
        return json.dumps(vars(self), indent=2)


class Event():
    def __init__(self):
        self.observers = []

    def signUp(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def trigger(self, change):
        for observer in self.observers:
            observer.update(change)


class Observer():
    filename = "data_observer.json"
    events = {"add": Logger.addToFile, "remove": Logger.addToFile}

    def update(self, change):
        item = self.events.get(change.name)
        if not item:
            return -1
        item(self.filename, change)
