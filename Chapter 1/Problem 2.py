# Install an external module and use it to perform an operation of your interest.

import pyttsx3 #It is a external library used to convert text into speach

engine = pyttsx3.init()
engine.say("This is my first text to speach python program")
engine.runAndWait()
