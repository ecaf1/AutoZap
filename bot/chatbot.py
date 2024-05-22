from app.DatabaseManeger import DatabaseManeger
from app.enums import Status 
from messageHandler import MessageHandler
class Chatbot:
    def __init__(self, database: DatabaseManeger, message_handler: MessageHandler):
        self.database = database
        self.message_handler = message_handler

    def run(self):
        while True:
            new_messages = self.database.get_new_messages()
            for message in new_messages:
                self.process_message(message)
                self.database.mark_processed(message[1])

    def process_message(self, message):
        if self.database.check_conversation_progress(message[1]):
            self.continue_conversation()
        else:
            self.start_conversation(message[1])

    def start_conversation(self, phone):
        self.message_handler.welcome_message(phone)
        self.database.update_conversation_status(phone, Status.start)

    def continue_conversation(self):
        pass
