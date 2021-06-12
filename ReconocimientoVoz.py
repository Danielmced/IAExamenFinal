import tkinter
import speech_recognition as speech_recog
from os import path
from tkinter import filedialog

class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.welcome = tkinter.Message(self)
        self.create_widgets()     

        
    def create_widgets(self):
        self.resultado = tkinter.Message(self)        
       
        try:
            self.resultado["text"] = ("Google Speech Recognition entiende que: " +
                recog.recognize_google(audio))
        except speech_recog.UnknownValueError:
            self.resultado["text"] = ("Google Speech Recognition no ha podido entender el audio")
        except speech_recog.RequestError as e:
            self.resultado["text"] = ("No ha se ha podido solicitar resultados a Google Speech Recognition service; {0}".format(e))
        self.resultado.pack(side="top")

        self.quit = tkinter.Button(self, text="QUIT", fg="red",
                                   command=self.master.destroy)
        self.quit.pack(side="bottom")

root = tkinter.Tk()
file_path = filedialog.askopenfilename(filetypes=(("wav files", "*.wav"), ("mp3 files", "*.mp3"),
                                       ("AAC files", "*.aac"), ("mp4 files", "*.mp4"), ("wma files", "*.wma"), ("all files", "*.*")))

AUDIO_FILE = path.join(path.dirname(
    path.realpath(__file__)), file_path)

recog = speech_recog.Recognizer()
with speech_recog.AudioFile(AUDIO_FILE) as source:
    audio = recog.record(source)

app = Application(master=root)
app.mainloop()

#Lo mismo pero en consola
try:
    print("Google Speech Recognition entiende que: " +
          recog.recognize_google(audio))
except speech_recog.UnknownValueError:
    print("Google Speech Recognition no ha podido entender el audio")
except speech_recog.RequestError as e:
    print("No ha se ha podido solicitar resultados a Google Speech Recognition service; {0}".format(e))
