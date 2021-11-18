from tkinter import *

import requests

clicks = 0
 

def click_button():
    global clicks
    clicks =requests.get('http://192.168.0.1/api/setLink?port=3&state=0')
   
    root.title("Clicks {}".format(clicks))
 
root = Tk()
root.title("PSW PoE")
root.geometry("300x250")
 
btn = Button( text="PoE off", background="#155", foreground="#fdc",
             padx="10", pady="105", font="666", command=click_button)

btn.pack()
 
root.mainloop()



