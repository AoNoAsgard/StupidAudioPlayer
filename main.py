import PIL._imaging
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
import audioplayer.audioplayer_windows


class Gui:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('200x300')

        self.thumbnail = ImageTk.PhotoImage(Image.open("assets/img/thumbnail.png").resize((200,200)))
        self.stop_img = ImageTk.PhotoImage(Image.open("assets/img/stop.png").resize((50,50)))
        self.play_img = ImageTk.PhotoImage(Image.open("assets/img/play.png").resize((50,50)))
        self.thumbnail_label = Label(self.root,image=self.thumbnail)
        self.thumbnail_label.grid(row = 0,column = 1)

        self.stop = True
        self.btn_stop = Button(self.root,image= self.play_img , command= self.stoplay)
        self.btn_stop.grid(row=1,column = 1)
        self.filename = filedialog.askopenfilenames(initialdir="/", title="Seleziona un file", filetypes=(
            ("mp3 files", "*.mp3"), ("wav files", "*.wav"), ("all files", "*.*")))

        self.play()
        self.player.play()
        self.player.stop()
        while True:
            try:
                self.root.update_idletasks()
                self.root.update()
            except TclError:
                exit()

    def stoplay(self):
        if self.stop:
            self.btn_stop.configure(image=self.stop_img)
            self.stop = False
            self.player.resume()
        else:
            self.btn_stop.configure(image=self.play_img)
            self.stop = True
            self.player.stop()


    def play(self):
        self.player = audioplayer.AudioPlayer(self.filename[0])

Gui()