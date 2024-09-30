import logging
from scrap_page import open_link, get_text_from_file, get_text_from_page
from audiobookconsol import make_audio_file

def main():
    logging.info("let's fun begin")
    link = input('give link: ')
    get_text_from_page(open_link(link))
    text = get_text_from_file('page')
    
    make_audio_file(text,'test3')
    logging.info("audiobook is complete :)")