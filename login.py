from tkinter import *
class login():
    def __init__(self, getName):
        self.master = Tk() 
        self.master.title('Chat Test')
        Label(self.master, text='Enter Your name').grid(row=0) 
        self.e1 = Entry(self.master) 
        self.button = Button(self.master, text="Start", command=lambda: getName(self), activebackground='Blue', activeforeground='blue', bg='black')
        self.e1.grid(row=0, column=1) 
        self.button.grid(row = 2, column=0, columnspan=2, sticky='ew')
        mainloop() 
                
    def end(self):
        self.master.destroy()