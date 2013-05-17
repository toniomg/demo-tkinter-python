from Tkinter import *

class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        Label(frame, text="Hello").pack(side=TOP);
        Button(frame, text="Quit", fg = "red", command = frame.quit).pack(side=LEFT)
        Button(frame, text="Hello", fg = "yellow", command = self.say_hi).pack(side=RIGHT)


    def say_hi(self):
        print "Hi"



root = Tk()

app = App(root)

root.mainloop()

