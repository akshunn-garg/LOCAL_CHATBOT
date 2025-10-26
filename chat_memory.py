class ChatMemory:
    def __init__(self,window_size=5):
        self.window_size=window_size
        self.history=[]

    def add(self,user_message,bot_message):
        self.history.append((user_message, bot_message))
        if len(self.history)>self.window_size:
            self.history.pop(0)

    def get_context(self):
        context=""
        for user,bot in self.history:
            context+=f"User: {user}\nBot: {bot}\n"
        return context
