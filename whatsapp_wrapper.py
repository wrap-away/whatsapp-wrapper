from webwhatsapi import WhatsAPIDriver


class WhatsappWrapper:
    def __init__(self, profile_path, username="kautilya", headless_flag=True):
        self.username = username
        self.profile_path = profile_path
        self.headless_flag = headless_flag
        self.driver = self.open()
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

    def open(self):
        driver = WhatsAPIDriver(username=self.username, profile=self.profile_path, headless=self.headless_flag,
                                loadstyles=True)
        driver.wait_for_login()
        return driver

    def close(self):
        return self.driver.close()


class Chat:
    def __init__(self, p_chat):
        split_text = p_chat.id.split("@")
        self.phone_number = split_text[0]
        self.chat_type = split_text[1]
        self.parent = p_chat
        self.loaded_messages = False

    def send_message(self, text):
        return self.parent.send_message(text)

    def get_messages(self):
        if self.loaded_messages:
            return self.parent.get_messages()
        self.parent.load_earlier_messages()
        self.loaded_messages = True
        return self.parent.get_messages()
