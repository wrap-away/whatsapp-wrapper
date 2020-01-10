from utils import get_response
from time import sleep
from whatsapp_wrapper import WhatsappWrapper

print("Starting selenium instance and logging to whatsap00p-web...")
profile_path = "/home/slapbot/.mozilla/firefox/xf0clnwz.whatsapp-user"
ww = WhatsappWrapper(profile_path)

print("Getting all chats...")
chats = ww.get_all_chats()
test_chat = chats[0]

global_cache = {}
print("Ready!")


def loop():
    print("Starting to look for new messages...")
    messages = test_chat.get_messages()
    last_message = messages[-1]
    last_message_timestamp = last_message.timestamp.timestamp()

    if last_message_timestamp in global_cache:
        print("No new message was found.")
        return

    print("A new message is found.")
    global_cache[last_message.timestamp.timestamp()] = 1

    resp = get_response(last_message.content)
    if resp is not False:
        print("Replying back the response as {}".format(resp))
        test_chat.send_message(resp)

    print("Message was an incorrect input.")

while True:
    loop()
    sleep(2)
