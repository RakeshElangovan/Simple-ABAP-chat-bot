import json
import random
from app.services.llm_service import LLMService


class ResponseGenerator:

    def __init__(self):
        with open("app/data/responses.json", "r") as file:
            self.responses = json.load(file)
        
        self.llm_service = LLMService()
        self.use_llm = self.llm_service.is_available()

    def generate_response(self, intent):
        
        # Get template/context for the intent
        template = None
        if intent in self.responses:
            template = random.choice(self.responses[intent])
        
        # If LLM is available, use it for dynamic responses
        if self.use_llm and template:
            prompt = f"The user has intent: {intent}. Based on this, provide a helpful response. Context: {template}"
            return self.llm_service.generate_response(prompt)
        
        # Fallback to template-based responses
        if template:
            return template
        
        return "Sorry, I did not understand."
