import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=880
        height=496
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_591=tk.Label(root)
        GLabel_591["anchor"] = "nw"
        ft = tkFont.Font(family='Times',size=22)
        GLabel_591["font"] = ft
        GLabel_591["fg"] = "#333333"
        GLabel_591["justify"] = "center"
        GLabel_591["text"] = "LocalBank"
        GLabel_591.place(x=0,y=0,width=193,height=79)

        GButton_183=tk.Button(root)
        GButton_183["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_183["font"] = ft
        GButton_183["fg"] = "#000000"
        GButton_183["justify"] = "center"
        GButton_183["text"] = "Login"
        GButton_183.place(x=20,y=100,width=150,height=50)
        GButton_183["command"] = self.GButton_183_command

        GButton_783=tk.Button(root)
        GButton_783["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_783["font"] = ft
        GButton_783["fg"] = "#000000"
        GButton_783["justify"] = "center"
        GButton_783["text"] = "Register"
        GButton_783.place(x=20,y=170,width=150,height=50)
        GButton_783["command"] = self.GButton_783_command

        GButton_202=tk.Button(root)
        GButton_202["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_202["font"] = ft
        GButton_202["fg"] = "#000000"
        GButton_202["justify"] = "center"
        GButton_202["text"] = "Exit"
        GButton_202.place(x=20,y=240,width=150,height=50)
        GButton_202["command"] = self.GButton_202_command

    def GButton_183_command(self):
        print("command")


    def GButton_783_command(self):
        print("command")


    def GButton_202_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
