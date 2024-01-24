# library to explore PDF files
from pdfquery import PDFQuery
# library  transform text to speech
from gtts import gTTS
# library that handles calls to the operating system
import os
import tkinter as tk
from tkinter import filedialog

# open a window for the user to select a file
root = tk.Tk()
root.withdraw()
full_file_name = filedialog.askopenfilename(parent=root, initialdir="/", title="Select file to convert", filetypes=[("pdf files", "*.pdf")] )
# print(full_file_name)

# Language of the text to convert
LANGUAGE = 'en'

# AI text-to-speech has come so far. They can sound more lifelike than a real audiobook.
# Using what you've learnt about HTTP requests, APIs and Python scripting, create a program that can convert PDF files to speech.
# You right want to choose your own Text-To-Speech (TTS) API. But here are some you can consider:
# http://www.ispeech.org/api/#introduction
# https://cloud.google.com/text-to-speech/docs/basics
# https://aws.amazon.com/polly/

try:
    pdf = PDFQuery(full_file_name)
except FileNotFoundError:
    print(f"File not found: {full_file_name}")
else:
    pdf.load()
    # convert to XML in order to be able to explore the CSS Selectors in use
    # pdf.tree.write(f'test_data/output.txt', pretty_print = True)

    # to get the text at a given location
    # text_parts = pdf.pq('LTTextLineHorizontal:in_bbox("72.024, 756.7, 318.865, 767.74")').text()

    # text elements are within a LTTextLineHorizontal markup
    text_result = pdf.pq('LTTextLineHorizontal').text()

    # print(text_result)

    voice_data = gTTS(text=text_result, lang=LANGUAGE, slow=False)
    voice_data.save(f'test_data/output.mp3')

    # Playing the converted file if the user requests ity
    listen = input("Do you want to listen to the result now? (y/n):")
    listen = listen.lower()[0]
    if listen == 'y':
        os.system(f'test_data\\output.mp3')