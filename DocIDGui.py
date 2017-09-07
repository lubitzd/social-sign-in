import Tkinter as tk

class DocIDGui(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createDocIDWidgets()
        self.createRegWidgets()

        self.switchFrames(self.docIDFrame)


    def switchFrames(self, frame):
        if frame == 'docID':
            self.docIDFrame.tkraise()
        elif frame == 'reg':
            self.regFrame.tkraise()


    def createDocIDWidgets(self):
        self.docIDFrame = tk.Frame(self)
        self.docIDFrame.grid(row=0, column=0)

        self.instructionsLabel = tk.Label(self.docIDFrame, text='[How to get Doc IDs]')
        self.instructionsLabel.grid(row=0, column=0, columnspan=2)

        self.masterLabel = tk.Label(self.docIDFrame, text='Master ID:')
        self.masterLabel.grid(row=1, column=0)
        self.danceLabel = tk.Label(self.docIDFrame, text='Dance ID:')
        self.danceLabel.grid(row=2, column=0)
        self.earlyLabel = tk.Label(self.docIDFrame, text='Early ID:')
        self.earlyLabel.grid(row=3, column=0)

        self.masterEntry = tk.Entry(self.docIDFrame, width=45)
        self.masterEntry.grid(row=1, column=1)
        self.danceEntry = tk.Entry(self.docIDFrame, width=45)
        self.danceEntry.grid(row=2, column=1)
        self.earlyEntry = tk.Entry(self.docIDFrame, width=45)
        self.earlyEntry.grid(row=3, column=1)
        
        self.goButton = tk.Button(self.docIDFrame, text='Go')
        self.goButton.grid(row=4, column=0, columnspan=2)


    def createRegWidgets(self):
        self.RegFrame = tk.Frame(self)
        self.RegFrame.grid(row=0, column=0)

        self.nameEntry = tk.Entry(self.RegFrame)
        self.nameEntry.grid(row=0, column=0)
        
