# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 21:07:28 2020

@author: aleks
"""

import os
import logging
import pyttsx3

engine = pyttsx3.init()

def make_audio_file(content:str, audio_file_name:str):
    logging.info("converting text to audio format")

    logging.info("setting rate")
    engine.setProperty('rate', 125)

    logging.info("setting volume")
    engine.setProperty('volume',1.0)

    logging.info('setting voice')
    voice = engine.getProperty('voices')
    engine.setProperty('voice',voice[0].id)

    engine.save_to_file(content, f"{audio_file_name}.mp3")
    engine.runAndWait()
    engine.stop()