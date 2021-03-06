#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
import os 
import speech_recognition as sr

from os import path
# Record Audio
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.record(source,duration=10)
 
path, dirs, files = os.walk(os.path.dirname(os.path.abspath(__file__))+ "/Enregistrements").next()
file_count = len(files)+1


audioFile=open("Enregistrements/Audio"+str(file_count)+".wav","w")

audioFile.write(audio.get_wav_data(convert_rate = None, convert_width = None))

audioFile.close()

# recognize speech using Google Speech Recognition
try:
# for testing purposes, we're just using the default API key
# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
# instead of `r.recognize_google(audio)`
  ficRep = open("Resultats/resultat.txt", "w")
  print("Ecriture fichier")
  ficRep.write( r.recognize_google(audio,language = "fr-FR"))
except sr.UnknownValueError:
  print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
  print("Could not request results from Google Speech Recognition service; {0}".format(e))

ficRep.close()