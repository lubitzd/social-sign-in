import Tkinter as tk


class DocIDPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.createDocIDWidgets()

    def createDocIDWidgets(self):
        self.rowconfigure(0, pad=5)
        self.rowconfigure(1, pad=5)
        self.rowconfigure(2, pad=5)
        self.rowconfigure(3, pad=5)
        self.rowconfigure(4, pad=5)
        self.columnconfigure(0, pad=5)
        
        instructionsLabel = tk.Label(self, text="To get the doc IDs, open the doc in your browser.\nThe part of the URL after the \"/d/\" and up to the next \"/\" is the ID.")
        instructionsLabel.grid(row=0, column=0, columnspan=2)

        masterLabel = tk.Label(self, text="Master ID:")
        masterLabel.grid(row=1, column=0)
        danceLabel = tk.Label(self, text="Dance ID:")
        danceLabel.grid(row=2, column=0)
        earlyLabel = tk.Label(self, text="Early ID:")
        earlyLabel.grid(row=3, column=0)

        # Master Doc ID
        self.masterDocIDVar = tk.StringVar()
        masterEntry = tk.Entry(self, width=45, textvariable=self.masterDocIDVar)
        masterEntry.grid(row=1, column=1, padx=5)
        # Dance Doc ID
        self.danceDocIDVar = tk.StringVar()
        danceEntry = tk.Entry(self, width=45, textvariable=self.danceDocIDVar)
        danceEntry.grid(row=2, column=1, padx=5)
        # Early Doc ID
        self.earlyDocIDVar = tk.StringVar()
        earlyEntry = tk.Entry(self, width=45, textvariable=self.earlyDocIDVar)
        earlyEntry.grid(row=3, column=1, padx=5)
        
        goButton = tk.Button(self, text="Go", command=lambda: self.controller.show_frame("IdlePage"))
        goButton.grid(row=4, column=0, columnspan=2)
