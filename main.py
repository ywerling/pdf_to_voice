# library to explore PDF files
from pdfquery import PDFQuery
# library  transform text to speech
from gtts import gTTS
import os

# Language of the text to convert
LANGUAGE = 'en'

# AI text-to-speech has come so far. They can sound more lifelike than a real audiobook.
# Using what you've learnt about HTTP requests, APIs and Python scripting, create a program that can convert PDF files to speech.
# You right want to choose your own Text-To-Speech (TTS) API. But here are some you can consider:
# http://www.ispeech.org/api/#introduction
# https://cloud.google.com/text-to-speech/docs/basics
# https://aws.amazon.com/polly/

pdf = PDFQuery('test_data/example_1.pdf')
pdf.load()
# convert to XML in order to be able to explore the CSS Selectors in use
pdf.tree.write('test_data/example_1.txt', pretty_print = True)

text_parts = pdf.pq('LTTextLineHorizontal:in_bbox("72.024, 756.7, 318.865, 767.74")').text()

print(text_parts)
# for text_element in text_parts:
#     print (text_element)


voice_data = gTTS(text=text_parts, lang=LANGUAGE, slow=False)
voice_data.save("test_data\wexample_1.mp3")

# Playing the converted file
os.system("test_data\wexample_1.mp3")