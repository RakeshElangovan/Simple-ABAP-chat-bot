import os
from ollama import Client


class LLMService:
    def __init__(self):
        self.server_url = os.getenv("OLLAMA_SERVER_URL", "http://localhost:11434")
        self.model = os.getenv("OLLAMA_MODEL", "mistral")
        self.client = Client(host=self.server_url)

    def generate_response(self, prompt: str, context: str = "") -> str:
        """
        Generate a response from the LLM based on the prompt and context.
        
        Args:
            prompt: The main prompt/query
            context: Optional context (e.g., detected intent, chat history)
            
        Returns:
            The generated response from the LLM
        """
        try:
            full_prompt = f"{context}\n\n{prompt}" if context else prompt
            
            response = self.client.generate(
                model=self.model,
                prompt=full_prompt,
                stream=False
            )
            
            return response.get("response", "").strip()
        
        except Exception as e:
            return f"Error generating response: {str(e)}"

    def is_available(self) -> bool:
        """Check if Ollama server is available."""
        try:
            self.client.list()
            return True
        except Exception:
            return False
