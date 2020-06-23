import tkinter as tk
import datetime
import time
import threading

class Timer:
    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root)
        self.label["font"] = ("Helvetica", 50)
        self.label["bg"] = "green"
        self.label["fg"] = "white"
        self.label.grid(column=0, row=0)

    def changeLabelText(self):
        while True:
            self.label["text"] = datetime.datetime.now().strftime("%H:%M:%S:%Q")
            time.sleep(0.1)

if __name__ == "__main__":
    timer = Timer()
    thread = threading.Thread(target=timer.changeLabelText)
    thread.start()
    timer.root.mainloop()