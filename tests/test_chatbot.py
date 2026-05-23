
from app.core.chatbot import ChatBot


def test_response():

    bot = ChatBot()

    response = bot.get_response("hello")

    assert response is not None
