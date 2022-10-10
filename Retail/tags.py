import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("QTY Update")
        #setting window size
        width=581
        height=505
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_115=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_115["font"] = ft
        GLabel_115["fg"] = "#333333"
        GLabel_115["justify"] = "center"
        GLabel_115["text"] = "Select your File"
        GLabel_115.place(x=60,y=290,width=91,height=42)

        GLineEdit_766=tk.Entry(root)
        GLineEdit_766["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_766["font"] = ft
        GLineEdit_766["fg"] = "#333333"
        GLineEdit_766["justify"] = "center"
        GLineEdit_766["text"] = " "
        GLineEdit_766.place(x=60,y=340,width=313,height=30)

        GButton_93=tk.Button(root)
        GButton_93["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_93["font"] = ft
        GButton_93["fg"] = "#000000"
        GButton_93["justify"] = "center"
        GButton_93["text"] = "select file"
        GButton_93.place(x=400,y=340,width=78,height=30)
        GButton_93["command"] = self.GButton_93_command

        GLabel_476=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_476["font"] = ft
        GLabel_476["fg"] = "#333333"
        GLabel_476["justify"] = "center"
        GLabel_476["text"] = "Database Link"
        GLabel_476.place(x=60,y=40,width=91,height=30)

        GLineEdit_db_Link=tk.Entry(root)
        GLineEdit_db_Link["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_db_Link["font"] = ft
        GLineEdit_db_Link["fg"] = "#333333"
        GLineEdit_db_Link["justify"] = "center"
        GLineEdit_db_Link["text"] = "localhost\sqlexpress2008r2"
        GLineEdit_db_Link.place(x=60,y=80,width=316,height=30)

        GLabel_348=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_348["font"] = ft
        GLabel_348["fg"] = "#333333"
        GLabel_348["justify"] = "center"
        GLabel_348["text"] = "Login info"
        GLabel_348.place(x=60,y=130,width=70,height=25)

        GLineEdit_576=tk.Entry(root)
        GLineEdit_576["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_576["font"] = ft
        GLineEdit_576["fg"] = "#333333"
        GLineEdit_576["justify"] = "center"
        GLineEdit_576["text"] = "sa"
        GLineEdit_576.place(x=60,y=160,width=179,height=30)

        GLineEdit_636=tk.Entry(root)
        GLineEdit_636["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_636["font"] = ft
        GLineEdit_636["fg"] = "#333333"
        GLineEdit_636["justify"] = "center"
        GLineEdit_636["text"] = "0000"
        GLineEdit_636.place(x=60,y=240,width=184,height=30)

        GLabel_136=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_136["font"] = ft
        GLabel_136["fg"] = "#333333"
        GLabel_136["justify"] = "center"
        GLabel_136["text"] = "Password"
        GLabel_136.place(x=60,y=210,width=70,height=25)

        GButton_257=tk.Button(root)
        GButton_257["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_257["font"] = ft
        GButton_257["fg"] = "#000000"
        GButton_257["justify"] = "center"
        GButton_257["text"] = "start"
        GButton_257.place(x=60,y=420,width=115,height=31)
        GButton_257["command"] = self.GButton_257_command

    def GButton_93_command(self):
        print("command")


    def GButton_257_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
