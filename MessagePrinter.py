class MessagePrinter:
    def __init__(self, message_type):
        self.message_type = message_type

    def printer(self, message):
        print(f"{self.message_type}: {message}")

assignment = MessagePrinter("Homework")
assignment.printer(input("Enter homework name"))