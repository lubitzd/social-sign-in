import Tkinter as tk


class DocIDPage(tk.Frame):
    def __init__(self, parent, controller, lc_in):
        tk.Frame.__init__(self, parent)
        self.lc = lc_in
        self.controller = controller
        self.createDocIDWidgets()


    def createDocIDWidgets(self):
        self.rowconfigure(0, pad=5)
        self.rowconfigure(1, pad=5)
        self.rowconfigure(2, pad=5)
        self.rowconfigure(3, pad=5)
        self.rowconfigure(4, pad=5)
        self.columnconfigure(0, pad=5)
        
        instructionsLabel = tk.Label(self, text="To get the doc IDs, open the doc in your browser.\nThe part of the URL after the \"/d/\" and up to the next \"/\" is the ID.", font=self.controller.customFont)
        instructionsLabel.grid(row=0, column=0, columnspan=2)

        masterLabel = tk.Label(self, text="Master ID:", font=self.controller.customFont)
        masterLabel.grid(row=1, column=0)
        danceLabel = tk.Label(self, text="Dance ID:", font=self.controller.customFont)
        danceLabel.grid(row=2, column=0)
        earlyLabel = tk.Label(self, text="Early ID:", font=self.controller.customFont)
        earlyLabel.grid(row=3, column=0)

        # Master Doc ID
        self.masterDocIDVar = tk.StringVar()
        if __debug__:
            self.masterDocIDVar.set("1BVedAhtD37Ocy4CGXiJPQ7Rrc8Va5G0akSqQVXFqS_0")
        masterEntry = tk.Entry(self, width=45, textvariable=self.masterDocIDVar, font=self.controller.customFont)
        masterEntry.grid(row=1, column=1, padx=5)
        # Dance Doc ID
        self.danceDocIDVar = tk.StringVar()
        if __debug__:
            self.danceDocIDVar.set("1f1XkRPCYjhU604NQoyxYRSk2kGxTr25rYCYz4pgcD-o")
        danceEntry = tk.Entry(self, width=45, textvariable=self.danceDocIDVar, font=self.controller.customFont)
        danceEntry.grid(row=2, column=1, padx=5)
        # Early Doc ID
        self.earlyDocIDVar = tk.StringVar()
        if __debug__:
            self.earlyDocIDVar.set("10goWvPEd8_n4Vd03PzXaukNX64rCMX0Tuzb55TR0u7M")
        earlyEntry = tk.Entry(self, width=45, textvariable=self.earlyDocIDVar, font=self.controller.customFont)
        earlyEntry.grid(row=3, column=1, padx=5)
        
        goButton = tk.Button(self, text="Go", command=self.goButtonCallback, font=self.controller.customFont)
        goButton.grid(row=4, column=0, columnspan=2)


    def goButtonCallback(self):
        self.controller.busy()
        # Print out Doc IDs so if user restarts, IDs are accessible
        print "Master: " + self.masterDocIDVar.get()
        print "Dance: " + self.danceDocIDVar.get()
        print "Early: " + self.earlyDocIDVar.get()
        self.lc.init_sheets(self.masterDocIDVar.get(), self.danceDocIDVar.get(), self.earlyDocIDVar.get())
        self.controller.not_busy()
        self.controller.show_frame("IdlePage")


    def populate(self):
        return
