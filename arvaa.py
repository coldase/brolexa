from random import randint
from mic import get_audio
import pyttsx3

def speak(text):
	engine.say(text)
	engine.runAndWait()

engine = pyttsx3.init()



def play_game():
	rand = randint(1,9)
	speak("Guess number between 1 and 9")
	while True:
		ask = get_audio()
		try:

			if int(ask) in range(1,10):
				if int(ask) > rand:
					speak(f"Guess lower")
					continue
				elif int(ask) < rand:
					speak(f"Guess higher")
					continue
				else:
					speak("Grats, You win")
					break
			else:
				speak("Please try again")
				continue
		except:
			speak("Please try again")
			continue