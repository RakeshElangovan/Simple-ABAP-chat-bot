from app.core.intent_engine import IntentEngine
from app.core.response_generator import ResponseGenerator
from app.core.memory_manager import MemoryManager


class ChatBot:

    def __init__(self):
        self.intent_engine = IntentEngine()
        self.response_generator = ResponseGenerator()
        self.memory_manager = MemoryManager()

    def get_response(self, user_message):

        intent = self.intent_engine.detect_intent(user_message)

        response = self.response_generator.generate_response(intent)

        self.memory_manager.save_chat(
            user_message,
            response
        )

        return response
