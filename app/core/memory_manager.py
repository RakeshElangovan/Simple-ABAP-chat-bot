import json
import os


class MemoryManager:

    def __init__(self):
        self.history_file = "app/data/chat_history.json"

    def save_chat(self, user_message, bot_response):

        history = []

        if os.path.exists(self.history_file):

            with open(self.history_file, "r") as file:
                try:
                    history = json.load(file)
                except:
                    history = []

        history.append({
            "user": user_message,
            "bot": bot_response
        })

        with open(self.history_file, "w") as file:
            json.dump(history, file, indent=4)
