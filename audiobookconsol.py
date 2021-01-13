# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 21:07:28 2020

@author: aleks
"""

import PyPDF2
from gtts import gTTS
import os




#print(pdfReader.numPages)

#pageObj = pdfReader.getPage(5)


#rint(pageObj.extractText())
#text = pageObj.extractText()

#language = 'en'

#myobj = gTTS(text=text, lang=language, slow=False)

#myobj.save("article.mp3")
def choosedFile(path):
    pdfFile = open(path,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    print(pdfReader.numPages)
    choosedFile.allPages = []
    countPage = pdfReader.numPages
    for i in range(0,countPage):
        page = pdfReader.getPage(i)
        string = page.extractText()
        choosedFile.allPages.append(string)
  
    return choosedFile.allPages

def fileToSpeech(text):
    myText = text
    language = 'en'
    full = ' '.join(myText)
     
    sound = gTTS(text=full, lang=language,slow=False)
    title = input("Nazwij plik: ")
    sound.save(title)
file = input("Podaj scieżkę dostępu do pliku: ")
choosedFile(file)
text = []
text = choosedFile.allPages
choose = input("Czy chcesz zapisać plik do formatu .mp3 t - tak, n - nie: ")
if choose == "t":
    fileToSpeech(text)

    