import requests
import logging
from gtts import gTTS
from bs4 import BeautifulSoup

'''
    step 1: get content from link
    step 2: seperate actual text from the rest
    step 3: turn text into audio
    step 4: save into file
'''

logging.basicConfig(level=logging.INFO)

def open_link(link:str) -> str:
    logging.info('open link')
    page_content = requests.get(link)
    return page_content.content

def get_text(content) -> str:
    logging.info('scraping text from link')
    soup = BeautifulSoup(content, 'html.parser')
    return soup.get_text()

def text_to_speech(content:str) -> gTTS:
    logging.info("converting text to audio format")
    lang = 'en'
    return gTTS(content,lang=lang,tld='com',slow=False)

def save_audio(audio: gTTS, title):
    logging.info("saving audio file")
    audio.save(title)

def main():
    logging.info("let's fun begin")
    link = 'https://lwn.net/Articles/988894/'
    text = get_text(open_link(link))
    save_audio(text_to_speech(text),'test.mp3')
    logging.info("audiobook is complete :)")

if __name__ == "__main__":
    main()