from webwhatsapi import WhatsAPIDriver


class WhatsappWrapper:
    def __init__(self, profile_path, username="kautilya"):
        self.driver = WhatsAPIDriver(username=username, profile=profile_path, loadstyles=True)
        self.driver.wait_for_login()
        self.chats = []

    def get_all_chats(self):
        if len(self.chats) > 0:
            return self.chats
        self.chats = self.process_chats(self.driver.get_all_chats())
        return self.chats

    @staticmethod
    def process_chats(chats):
        chats = [Chat(chat) for chat in chats]
        return chats


class Chat:
    def __init__(self, p_chat):
        split_text = p_chat.id.split("@")
        self.phone_number = split_text[0]
        self.chat_type = split_text[1]
        self.parent = p_chat

    def send_message(self, text):
        return self.parent.send_message(text)
