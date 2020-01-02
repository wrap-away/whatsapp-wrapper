from whatsapp_wrapper import WhatsappWrapper

profile_path = "/home/slapbot/.mozilla/firefox/xf0clnwz.whatsapp-user"
ww = WhatsappWrapper(profile_path)

chats = ww.get_all_chats()
chats[0].send_message("Saaaar!")
