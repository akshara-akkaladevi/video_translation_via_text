from gtts import gTTS

language = "en"
text = "hello world,real world video translation"
speech = gTTS(text=text, lang=language, slow=False)
speech.save("textToSpeech.mp3")

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source: 
    print("Speak now!") 
    audio = r.listen(source)
    speech_text = r.recognize_google (audio)
    print(speech_text)