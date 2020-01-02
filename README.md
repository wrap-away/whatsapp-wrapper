# Whatsapp Wrapper

A small wrapper around whatsapp web API using https://github.com/mukulhase/WebWhatsapp-Wrapper with clear instructions
on how to install properly.

## Installation

## System Setup:

1. Download Firefox 61.0.2: https://sourceforge.net/projects/ubuntuzilla/files/mozilla/apt/pool/main/f/firefox-mozilla-build/firefox-mozilla-build_61.0.2-0ubuntu1_amd64.deb/download
2. Uninstall Firefox if its already installed: `sudo apt-get purge firefox`
3. Remove any Mozilla configuration folder in home (~) if it exists otherwise it will keep crashing the browser: `sudo rm -rf .mozilla`
4. Extract and then install using: `sudo dpkg -i firefox-mozilla-build_61.0.2-0ubuntu1_amd64.deb`
5. Download Geckodriver 0.21: https://github.com/mozilla/geckodriver/releases/tag/v0.21.0
6. Put it in path or move it to: `sudo mv geckodriver /usr/local/bin/`
7. Open firefox and go to `about:profiles`
8. Create a new profile, say name: `whatsapp-user` and then Copy that profile path, example: `/home/slapbot/.mozilla/firefox/xf0clnwz.whatsapp-user`
9. Open the profile and sign-in to https://web.whatsapp.com

## Application Setup

1. Clone this github repo: https://github.com/wrap-away/whatsapp-wrapper/
2. Cd in to the folder and create a virtualenv: `virtualenv whatsapp-wrapper-env`
3. Activate the env: `source whatsapp-wrapper-env/bin/activate`
4. Install WebWhatsapp-Wrapper from Github and not the pip: `pip install https://github.com/mukulhase/WebWhatsapp-Wrapper/archive/master.zip`
5. Install numpy: `pip install numpy`
6. Copy that profile_path name to `index.py` with has an existing example to showcase.


## Usage

Instantiate the wrapper:

```
from whatsapp_wrapper import WhatsappWrapper


profile_path = "/home/slapbot/.mozilla/firefox/xf0clnwz.whatsapp-user"
ww = WhatsappWrapper(profile_path)
```

Get all chats (Its necessary to get specific chat_ids in order to read/send messages:

```
chats = ww.get_all_chats()
chats[0].send_message("Saaaar!")
```
