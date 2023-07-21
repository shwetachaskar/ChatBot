import random
import datetime
import webbrowser
import pyttsx3
import wikipedia
from pygame import mixer
#import speech_recognition as sr



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 25)

