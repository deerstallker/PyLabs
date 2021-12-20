from tkinter import *
from tkinter import messagebox
import tkinter as tk
import time
import requests


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.place()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self, font="Verdana", bg="red", fg="black", width=17, height=4)
        self.hi_there["text"] = "Link OFF"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.hi2_there = tk.Button(self, font="Verdana", bg="red", fg="black", width=17, height=4)
        self.hi2_there["text"] = "PoE OFF"
        self.hi2_there["command"] = self.say_hi
        self.hi2_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", font="Arial", fg="red", bg="white",  width=17,height=4, command=root.destroy)
        self.quit.pack(side="bottom")

        self.button = tk.Button(self, font="Verdana", bg="green", fg="black", width=17, height=4)
        self.button['text'] = time.strftime('%H:%M:%S')
        self.button['command'] = self.button_clicked
        self.button.pack(side="bottom")

        self.name_entry = Entry()
        self.name_entry.place(x=90, y=452)

        self.hi3_there = tk.Button(self, font="Verdana", bg="red", fg="black", width=17, height=4)
        self.hi3_there["text"] = "Записать"
        self.hi3_there["command"] = self.say_hi
        self.hi3_there.pack(side="bottom")

    def say_hi(self):
        print("text after press the button", 'http://{}/api/setLink?port=1&state=0'.format(self.name_entry.get()))
        clicks =requests.get('http://{}/api/setLink?port=1&state=0'.format(self.name_entry.get()))


    def button_clicked(self):
        self.button['text'] = time.strftime('%H:%M:%S')
  

root = tk.Tk()
root.title("PSW PoE")
root.geometry("300x650")
app = Application(master=root)
app.mainloop()
