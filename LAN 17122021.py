from tkinter import *
from tkinter import messagebox
import tkinter as tk
import time
import requests


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid()
        self.place()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self, font="Verdana", bg="red", fg="black", width=17, height=4)
        self.hi_there["text"] = "Link OFF"
        self.hi_there["command"] = self.say_hi
        self.hi_there.grid(row=0, column=0)

        self.hi2_there = tk.Button(self, font="Verdana", bg="red", fg="black", width=17, height=4)
        self.hi2_there["text"] = "PoE OFF"
        self.hi2_there["command"] = self.say_hi
        self.hi2_there.grid(row=5, column=0)

        self.hi3_there = tk.Button(self, font="Verdana", bg="red", fg="black", width=17, height=4)
        self.hi3_there["text"] = "Link OFF"
        self.hi3_there["command"] = self.say_hi
        self.hi3_there.grid(row=0, column=6)

        self.hi4_there = tk.Button(self, font="Verdana", bg="green", fg="black", width=17, height=4)
        self.hi4_there["text"] = "PoE ON"
        self.hi4_there["command"] = self.say_hi
        self.hi4_there.grid(row=5, column=6)

        self.hi5_there = tk.Button(self, font="Verdana", bg="red", fg="black", width=17, height=4)
        self.hi5_there["text"] = "Link OFF"
        self.hi5_there["command"] = self.say_hi
        self.hi5_there.grid(row=0, column=12)

        self.hi6_there = tk.Button(self, font="Verdana", bg="red", fg="black", width=17, height=4)
        self.hi6_there["text"] = "PoE OFF"
        self.hi6_there["command"] = self.say_hi
        self.hi6_there.grid(row=5, column=12)

        self.hi7_there = tk.Button(self, font="Verdana", bg="green", fg="black", width=17, height=4)
        self.hi7_there["text"] = "Link ON"
        self.hi7_there["command"] = self.say_hi
        self.hi7_there.grid(row=0, column=16)

        self.hi8_there = tk.Button(self, font="Verdana", bg="red", fg="black", width=17, height=4)
        self.hi8_there["text"] = "PoE OFF"
        self.hi8_there["command"] = self.say_hi1
        self.hi8_there.grid(row=5, column=16)

        self.quit = tk.Button(self, text="Выход", font=("Verdana",12), fg="red", bg="white", width=17, height=4,
                              command=root.destroy)
        self.quit.grid(row=45, column=16)

        self.button = tk.Button(self, font="Verdana", bg="green", fg="black", width=17, height=4)
        self.button['text'] = time.strftime('%H:%M:%S')
        self.button['command'] = self.button_clicked
        self.button.grid(row=25, column=16)

        self.label = tk.Label(text="Введите IP адрес PSW",font =("Verdana",15))
        self.label.place(x=172, y=220)
        self.name_entry = Entry(font =("Verdana",22),bd = 15,width = 15)
        self.name_entry.place(x=147, y=250)


    def say_hi(self):
        print('http://{}/api/setLink?port=1&state=0'.format(self.name_entry.get()))

        #clicks = requests.get('http://{}/api/setLink?port=1&state=0'.format(self.name_entry.get()))
    def say_hi1(self):
        print('http://{}/api/setPoe?port=1&state=0'.format(self.name_entry.get()))
        #clicks = requests.get('http://{}/api/setLink?port=1&state=0'.format(self.name_entry.get()))

    def button_clicked(self):
        self.button['text'] = time.strftime('%H:%M:%S')


root = tk.Tk()
root.title("TFortis PSW Only")
root.geometry("750x350")
app = Application(master=root)
app.mainloop()
