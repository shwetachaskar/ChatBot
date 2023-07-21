import speech_recognition as s
sr=s.Recognizer()
sr.pause_threshold=1
print('your bot is listening try to speak')
with s.Microphone() as m:
    audio=sr.listen(m)
    query=sr.recognize_google(audio,language='eng-in')
    print(query)