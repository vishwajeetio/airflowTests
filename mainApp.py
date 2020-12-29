'''Import dependencies''' 
from gtts import gTTS
from playsound import playsound

audio = 'data/speech.mp3'
language = 'en'
sp = gTTS(text = 'Airflow has a simple plugin manager built-in that can integrate external features to its core by simply dropping files in your $ AIRFLOW underscore HOME forward slash plugins folder. The python modules in the plugins folder get imported, and macros and web views get integrated to Airflow\'s main collections and become available for use.', lang = language, slow = False)
sp.save(audio)
playsound(audio)