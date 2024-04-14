from tkinter import *
import os
from tkinter import *
import sys
sys.path.insert(0, 'gTTS-2.4.0')
sys.path.insert(0, 'SpeechRecognition-3.10.0')
import speech_recognition as sr
from gtts import gTTS
class App:
    _titulo = "Texto a voz"
    _dictado = ""

    def __init__(self, master):
        ventana = Frame(master)
        ventana.pack()
        self.caja1 = Text(ventana, width=10, height=1)
        self.escucha = Button(ventana, text="Escuchar", command=self.escuchar)
        self.habla = Button(ventana, text="Hablar", command=self.hablar)
        self.label1 = Label(ventana, text=self._titulo)
        self.label1.pack(side=TOP)
        self.caja1.pack(pady=10)
        self.habla.pack(pady=10)
        self.escucha.pack(pady=15)
        self.label2 = Label(ventana, text=self._dictado)
        self.label2.pack(pady=20)

    def escuchar(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Habla ahora.")
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            self.label1.config(text=text) 
            print(text)
        except sr.UnknownValueError:
            print("No se entiende el audio")
        except sr.RequestError as e:
            print("No se pueden obtener los resulados de Google Speech Recognition; {0}".format(e)) 

    def hablar(self):
        texto_a_leer = self.caja1.get("1.0", END).strip()
        if texto_a_leer:
            tts = gTTS(text=texto_a_leer, lang='es')
            tts.save("temp.mp3")
            os.system("start temp.mp3")

root = Tk()
app = App(root)
root.mainloop()
