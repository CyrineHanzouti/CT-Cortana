#My Libs
import tkinter as tk
from tkinter import ttk
import webbrowser
import speech_recognition as sr
import urllib.request
import pyttsx3
import re
import os
import requests
import pygame

# Function to make the assistant speak
import io
import requests
import pygame

# Function to make the assistant speak
def say(text):
    # Make an HTTP request to the Google TTS API to generate speech for the given text
    r = requests.get(f"https://translate.google.com/translate_tts?ie=UTF-8&q={text}&tl=en&client=tw-ob")
    # Create an IO buffer to hold the audio data returned by the API
    audio_file = io.BytesIO(r.content)
    # Play the audio using pygame
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

# Function to make the assistant speak
#def say(text):
 #   engine.setProperty('rate', 170)
  #  engine.say(text)
   # engine.runAndWait()

# Function to open a YouTube search with the user query
def open_Youtube_search(query):
    query = query.lower()
    query = query.replace(" ", "+")
    url = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={query}")
    video_ids = re.findall(r"watch\?v=(\S{11})", url.read().decode())
    search_link = f"https://www.youtube.com/watch?v={video_ids[0]}"
    webbrowser.open(search_link)

# Function to open a Google search with the user query
def open_Google_search(query):
    query = query.lower()
    query = urllib.parse.quote(query)
    url = "https://www.google.com/search?q=" + query
    webbrowser.open(url)

# Function to open a program with the given program_name
def open_program(program_name):
    os.startfile(program_name)

# Function to work with the user request
def speaker():
    say("Hello, I'm CT-Cortana. What would you like me to search for?")
    query = recognize_speech()
    label.config(text=f"You said: {query}")
    window.update()
    say(f"Where would you like me to search {query} in? Choose YouTube or Google or a Windows program.")
    service = recognize_speech()
    label.config(text=f"You chose {service}")
    window.update()
    if service.lower() == "youtube":
        open_Youtube_search(query)
    elif service.lower() == "google":
        open_Google_search(query)
    else:
        open_program(query)
    label.config(text="Now You Can Use CT-Cortana")
    window.update()
# Function to recognize the user speech
def recognize_speech():
    label.config(text="Speak now...")
    window.update()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        text = ""
        while not text:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language="fr-FR")
                say("You said: " + text)
            except sr.UnknownValueError:
                label.config(text="Could not understand audio")

    return text
# Set the engine to use it in the function say
engine = pyttsx3.init()

# tkinter part (Graphique)
window = tk.Tk()
window.title("CT-Cortana")
window.geometry("300x300")
window.resizable(False, False)
window.config(bg='#FFF')

label = ttk.Label(background="#FFF" ,text="Now You Can Use CT-Cortana", font=("Arial", 12))
label.pack(pady=10)

button_img = tk.PhotoImage(file = 'voice.png',)
speak_button = tk.Button(window,background="#FFF",border=0 ,image=button_img , command=speaker).place(x=70,y=60)

window.mainloop()

