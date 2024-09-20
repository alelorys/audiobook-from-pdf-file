import requests
import re
from typing import List
from gtts import gTTS
from bs4 import BeautifulSoup

'''
    step 1: get content from link
    step 2: seperate actual text from the rest
    step 3: turn text into audio
    step 4: save into file
'''
def open_link(link:str) -> str:
    page_content = requests.get(link)
    return page_content.content

def get_text(content) -> str:
    soup = BeautifulSoup(content, 'html.parser')
    return soup.get_text()

def text_to_speech(content:str) -> gTTS:
    lang = 'en'
    return gTTS(content,lang=lang,slow=False)

def save_audio(audio: gTTS, title):
    audio.save(title)

def main():
    link = 'https://lwn.net/Articles/988894/'
    text = get_text(open_link(link))
    save_audio(text_to_speech(text),'test.mp3')

if __name__ == "__main__":
    main()