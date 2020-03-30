import tkinter as tk
from threading import Thread

class chatBox():
    def __init__(self, username, buttonFunction):
        self.tk = tk
        self.master = tk.Tk()
        self.master.title("Hi " + username + "!") 
        self.scrollbar = tk.Scrollbar(self.master) 
        self.mylist = tk.Listbox(self.master, yscrollcommand = self.scrollbar.set, width=50, height=30) 
        self.text = tk.Text(self.master, height=4, width=50) 
        self.button = tk.Button(self.master, text='Send', command=lambda: buttonFunction(self)) 

    def start(self, manageChat):
        self.mylist.grid(row = 0, column = 0, columnspan=2)
        self.scrollbar.grid(row = 0, column = 3, sticky='ns') 
        self.text.grid(row = 1, column=0, sticky='ew')
        self.button.grid(row = 1, column=1, columnspan=3, sticky="ewns")
        self.scrollbar.config( command = self.mylist.yview )
        while True:
            manageChat(self)
            self.master.update_idletasks()
            self.master.update()
            
    def end(self):
        self.master.destroy()