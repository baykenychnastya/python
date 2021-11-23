import json
import numpy as np


class Logger():
    @staticmethod
    def addToFile(filename, items):
        events = []

        with open(filename, 'r', encoding='utf-8') as f:
            eventsJson = json.load(f)
            for eventJson in eventsJson:
                events.append(eventJson)
        events.append(items.options)
        with open(filename, 'w', encoding='utf-8') as f:
            # events.append(items)
            f.write(json.dumps(events, indent=2))
