class MemoryAgent:

    def __init__(self):
        self.memory = {}

    def save_conversation(self, user_id, conversation):
        self.memory[user_id] = conversation

    def get_memory(self, user_id):
        return self.memory.get(user_id, [])