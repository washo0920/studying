import tkinter as tk
from tkinter import messagebox as mbox

win = tk.Tk()
win.title("Hello,World")
win.geometry("500x250")
win.config(bg="#303030")

label = tk.Label(win,text = "名前は？")
label.pack()
label.config(bg="#303030",fg="#FFFFFF")

text = tk.Entry(win)
text.pack()
text.insert(tk.END,"クジラ")

def ok_click():
    s = text.get()
    mbox.showinfo("挨拶",s + "さんこんいちは")

okButton = tk.Button(win,text="OK",command = ok_click)
okButton.pack()

win.mainloop()