import speech_recognition as sr

def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		if audio:
			try:
				text = r.recognize_google(audio)
				return text
			except:
				return ""
		else:
			pass

