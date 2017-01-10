# coding: utf-8
from __future__ import with_statement
import speech_recognition as sr
from os import path
import requests
import os
import time
from pydub import AudioSegment
from pydub.playback import play
from pydub import AudioSegment
from gtts import gTTS


etatpresent = -1
interact = 0
boisson = 0
question = 0
pascompris = 0
neg = 0
autorisation = 0
demarrage = 0


"""
Etats :

0 : attente arrivée signal vocal
1 : Extraction information de la phrase --> question, choix boisson, ou pas compris
2 : Réponse question
3 : Vérification négation
4 : Réponse à négation
5 : Vérification autorisation
6 : Réponse à boisson non autorisée
7 : Vérification stock
8 : Réponse pas en stock
9 : Service de la boisson "Voici votre commande ..."

"""


while 1:


	if etatpresent == -1:

		if demarrage == 1:
			etatsuivant = 0
		else:
			etatsuivant = -1

	if etatpresent == 0:

		if interact ==1:
			etatsuivant = 1
		else:
			etatsuivant = 0

	if etatpresent == 1:

		if boisson == 1:
			etatsuivant = 3
		if question == 1:
			etatsuivant = 2
		if pascompris == 1:
			etatsuivant = 0

	if etatpresent == 2:

		etatsuivant = 0
		
	if etatpresent == 3:

		if neg == 1:
			etatsuivant = 4
		if neg == 0:
			etatsuivant = 5
		
	if etatpresent == 4:

		etatsuivant = 0
		
	if etatpresent == 5:

		if autorisation == 1:
			etatsuivant = 7
		if autorisation == 0:
			etatsuivant = 6
		
	if etatpresent == 6:

		etatsuivant = 0
		
	if etatpresent == 7:

		if stock == 1:
			etatsuivant = 9
		if stock == 0:
			etatsuivant = 8
		
	if etatpresent == 8:

		etatsuivant = 0

	if etatpresent == 9:

		etatsuivant = 0

	


	etatpresent = etatsuivant


	if etatpresent == -1:

		demarrage = 1

		txt = "Bonjour, que puis-je pour vous ?"

		tts = gTTS(text=txt, lang='fr')
        	tts.save("question.mp3")

		song = AudioSegment.from_mp3("question.mp3")
        	play(song)


	if etatpresent == 0:

		pascompris = 0		

		#txt = "Bonjour, je voudrais une bierre"
		#txt = "Bonjour, je veux des faritas"

        	#tts = gTTS(text=txt, lang='fr')
        	#tts.save("question.mp3")


		#sound = AudioSegment.from_mp3("question.mp3")
		#sound.export("/home/ubunturos/Documents/question", format="wav")

		#song = AudioSegment.from_mp3("question.mp3")
        	#play(song)



		#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "question") 
		# Record Audio
		r = sr.Recognizer()
		
		interact = 1


	if etatpresent == 1:

		interact = 0

		#with sr.AudioFile(AUDIO_FILE) as source:
		#	audio = r.record(source)

		with sr.Microphone() as source:
    			print("Say something!")
    			audio = r.listen(source)

		# recognize speech using Google Speech Recognition
		try:
		# for testing purposes, we're just using the default API key
		# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
		# instead of `r.recognize_google(audio)`

  			ficRep = open("resultat.txt", "w")
  			print("Ecriture fichier")
			phrase = r.recognize_google(audio,language = "fr-FR")
			print phrase
			phrase = str(phrase)
			print( phrase)
  			ficRep.write( r.recognize_google(audio,language = "fr-FR"))
		except sr.UnknownValueError:
  			print("Google Speech Recognition could not understand audio")
		except sr.RequestError as e:
  			print("Could not request results from Google Speech Recognition service; {0}".format(e))

		ficRep.close();

		
		
		mots = phrase.split()
		choixboisson = ""


		for mot in mots:

			print mot

			if str(mot) == "jus":
				for mot1 in mots:
					if mot1 == "pomme" or mot1 == "raisin" or mot1 == "d'orange" or mot1 == "poire":
						boisson = 1
						choixboisson = choixboisson + " jus de " + str(mot1)

			elif str(mot) == "l'eau" or str(mot) == "coca" or str(mot) == "vin" or str(mot) == "bierre" or str(mot) == "whisky":
				boisson = 1

				choixboisson = choixboisson + " " + str(mot)

				print choixboisson

			elif str(mot) == "fruit" or str(mot) == "fruits" or str(mot) == "quel" or str(mot) == "qu'est-ce" or str(mot) == "qu'avez-vous" or str(mot) == "que" or str(mot) == "boisson" or str(mot) == "boire":

				for mot1 in mots:
					if mot1 == "fruit":
						choixboisson = str(mot1)

				if choixboisson != "fruit":
					choixboisson = "boisson"

				question = 1
				boisson = 0

		print question
		print choixboisson

		if boisson == 0 and question == 0:
			pascompris = 1

			txt = "Veuilez m'excuser, je ne commprend pas votre commande"

			tts = gTTS(text=txt, lang='fr')
       			tts.save("reponse.mp3")

			song = AudioSegment.from_mp3("reponse.mp3")
       			play(song)

		
		
	if etatpresent == 2:

		question = 0

		if choixboisson == "fruit":
			txt = "Nous avons du jus d'orange, de pomme, de poire et de raisin"
			print txt
		if choixboisson == "boisson":
			txt = "Nous avons des jus de fruit, et des sodas"
			print txt

		tts = gTTS(text=txt, lang='fr')
        	tts.save("reponse.mp3")

		song = AudioSegment.from_mp3("reponse.mp3")
        	play(song)
		

	if etatpresent == 3:

		boisson = 0

		for mot in mots:

			if str(mot) == "non" or str(mot) == "ne" or str(mot) == "n" or str(mot) == "pas":
				neg = 1

		
		
	if etatpresent == 4:

		neg = 0

		txt = "Quelle boisson souhaitez vous commander ?"

		tts = gTTS(text=txt, lang='fr')
        	tts.save("reponse.mp3")

		song = AudioSegment.from_mp3("reponse.mp3")
        	play(song)

		
		
	if etatpresent == 5:

		if choixboisson == " vin" or choixboisson == " bierre" or choixboisson == " whisky":
			autorisation = 0
		else:
			autorisation = 1
		

	if etatpresent == 6:

		txt = "Je suis désolé mais nous ne servons pas d'alcool sur le campus. Que puis-je vous servir d'autre ?"

		tts = gTTS(text=txt, lang='fr')
        	tts.save("reponse.mp3")

		song = AudioSegment.from_mp3("reponse.mp3")
        	play(song)

		
		
	if etatpresent == 7:

		#stockcoca = stock[0]
		#stockpomme = stock[1]
		#stockorange = stock[2]
		#stockraisin = stock[3]
		#stockorange = stock[4]
		#stockpoire = stock[5]

		stockboisson =  [1,0,1,2,3,0]

		mots = choixboisson.split()

		for mot in mots:

			if str(mot) == "jus":
				for mot1 in mots:
					if mot1 == "pomme" or mot1 == "raisin" or mot1 == "orange" or mot1 == "poire":
						txt = "jus de " + mot1

			elif str(mot) == "l'eau" or str(mot) == "coca":
				txt = str(mot)

		if txt == "coca":
			quantite = stockboisson[0]
		elif txt == "jus de pomme":
			quantite = stockboisson[1]
		elif txt == "jus de raisin":
			quantite = stockboisson[2]
		elif txt == "jus de orange":
			quantite = stockboisson[3]
		elif txt == "l'eau":
			quantite = stockboisson[4]
		elif txt == "jus de poire":
			quantite = stockboisson[5]
		else:
			quantite = 0

		if quantite == 0:
			stock = 0
		else:
			stock = 1
			
		
	if etatpresent == 8:

		txt = "Je suis vraiment désolé mais nous n'en avons plus. Voulez vous une autre boisson ?"

		tts = gTTS(text=txt, lang='fr')
        	tts.save("reponse.mp3")

		song = AudioSegment.from_mp3("reponse.mp3")
        	play(song)


	if etatpresent == 9:

		# commande service de boisson

		txt = "Voici votre"

		#print "choix boisson : " + choixboisson

		mots = choixboisson.split()

		for mot in mots:

			if str(mot) == "jus":
				for mot1 in mots:
					if mot1 == "pomme" or mot1 == "raisin" or mot1 == "orange":
						if txt != "Voici votre":
							txt = txt + " et votre jus de " + mot1
						if txt == "Voici votre":
							txt = txt + " jus de " + mot1

			elif str(mot) == "eau" or str(mot) == "coca" or str(mot) == "vin" or str(mot) == "bierre":
				if txt != "Voici votre":
					txt = txt + " et votre " + str(mot)
				if txt == "Voici votre":
					txt = txt + str(mot)

		#print "Phrase : " + txt

		

		tts = gTTS(text=txt, lang='fr')
        	tts.save("reponse.mp3")

		song = AudioSegment.from_mp3("reponse.mp3")
        	play(song)


