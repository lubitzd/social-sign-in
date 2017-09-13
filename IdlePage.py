import Tkinter as tk
import tkFont


# Hangs out and then finds what row in the sheet to pull
class IdlePage(tk.Frame):
    def __init__(self, parent, controller, lc_in):
        tk.Frame.__init__(self, parent)
        self.lc = lc_in
        self.controller = controller
        self.createIdleWidgets()

    def createIdleWidgets(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)

        scanLabel = tk.Label(self, text="Scan a card", font=tkFont.Font(size=14))
        scanLabel.grid(row=0, column=1)

        or1Label = tk.Label(self, text="or")
        or1Label.grid(row=1, column=1, pady=5)

        newButton = tk.Button(self, text="New Account", command=self.newAccountCallback)
        newButton.grid(row=2, column=1, ipady=5, ipadx=10)

        or2Label = tk.Label(self, text="or")
        or2Label.grid(row=3, column=1, pady=5)

        nameLabel = tk.Label(self, text="Name:")
        nameLabel.grid(row=4, column=0, sticky="e")

        self.nameVar = tk.StringVar()
        nameEntry = tk.Entry(self, textvariable=self.nameVar)
        nameEntry.grid(row=4, column=1, padx=5)

        searchButton = tk.Button(self, text="Search", command=self.searchByNameCallback)
        searchButton.grid(row=4, column=2, sticky="w")

        self.errorLabelVar = tk.StringVar()
        self.errorLabelVar.set("No match found")
        self.errorLabel = tk.Label(self, textvariable=self.errorLabelVar, fg="#EB1717")
        self.errorLabel.after(1000, self.hideErrorLabel)
        self.errorLabel.grid(row=5, column=1, pady=2, sticky="n")


    def hideErrorLabel(self):
        self.errorLabelVar.set("")


    # Find the next open row in the master sheet
    def newAccountCallback(self):
        row = self.lc.find_open_row("master")
        self.lc.set_current_row(row)
        self.controller.show_frame("RegPage")


    def searchByNameCallback(self):
        
        (already_logged, index) = self.lc.search("Name", self.nameVar.get())
        if index == -1:
            self.errorLabelVar.set("No match found")
            self.errorLabel.after(6000, self.hideErrorLabel)

        self.controller.show_frame("RegPage")

