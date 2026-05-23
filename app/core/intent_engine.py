import json


class IntentEngine:

    def __init__(self):
        with open("app/data/intents.json", "r") as file:
            self.intents = json.load(file)

    def detect_intent(self, message):

        message = message.lower()

        for intent, keywords in self.intents.items():

            for keyword in keywords:

                if keyword in message:
                    return intent

        return "unknown"
