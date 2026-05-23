import logging


logging.basicConfig(
    filename="chatbot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class LoggerService:

    @staticmethod
    def log(message):
        logging.info(message)
