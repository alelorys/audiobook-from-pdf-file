import requests
import logging
from bs4 import BeautifulSoup

'''
    step 1: get content from link
    step 2: seperate actual text from the rest
    step 3: turn text into audio
    step 4: save into file
'''

logging.basicConfig(level=logging.INFO)
tags_to_remove = ['<p>','</p>','<q>','</q>']

def open_link(link:str) -> str:
    logging.info('open link')
    page_content = requests.get(link)
    return page_content.content

def get_text_from_page(content) -> str:
    logging.info('scraping text from link')
    soup = BeautifulSoup(content, 'html.parser')
    paras = soup.find_all('p')
    paras = "".join(str(paras))

    for tag in tags_to_remove:
        paras = paras.replace(tag,'')

    with open('page.txt','w',encoding='utf-8') as f:
        f.writelines(paras)
    return paras

def get_text_from_file(file_name):
    with open(f'{file_name}.txt', 'r') as file:
        content = file.readlines()

        return "".join(content)
    