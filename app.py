import pyttsx3
import datetime
import requests
import json
from mic import get_audio
import webbrowser
import time
from arvaa import play_game

engine = pyttsx3.init()

def print_screen(msg):
	for x in range(80):
		print("")
	print(f'{msg}\n')

def get_jokes():
	url = "https://icanhazdadjoke.com/"
	res = requests.get(url, headers={"Accept":"application/json"})
	data = json.loads(res.text)
	return data

def speak(text):
	print_screen(text)
	engine.say(text)
	engine.runAndWait()
	

speak("Hello, i am  Bro-lexa, your assistant")
def brolexa(default_message="Choose application"):
	speak(default_message)
	ask = get_audio()
	if ask.lower() == "exit":
		speak("Shutting down, bye bye")
	elif ask.lower() == "clock":
		time_atm = datetime.datetime.now()
		speak(f'Clock is {time_atm.hour}:{time_atm.minute}')
		brolexa()
	elif ask.lower() == "google":
		speak("What you want to search")
		try:
			ask_term = get_audio()
			speak(f"Searching for {ask_term}")
			webbrowser.open(f"https://google.com/search?q={ask_term}&oq={ask_term}")
			brolexa()
		except:
			speak("Couldnt understand, try again")
			brolexa()
	elif ask.lower() == "joke":
		joke = get_jokes()
		speak(joke["joke"])
		time.sleep(1)
		brolexa()
	elif ask.lower() == "play":
		play_game()
		brolexa()
	else:
		brolexa(f"Couldnt find {ask}, Try again")
	
brolexa()