import Tkinter as tk
import tkFont


class IdlePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.createIdleWidgets()

    def createIdleWidgets(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.columnconfigure(0, weight=1)
        #self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        scanLabel = tk.Label(self, text="Scan a card", font=tkFont.Font(size=14))
        scanLabel.grid(row=0, column=1)

        or1Label = tk.Label(self, text="or")#, font=tkFont.Font(size=14))
        or1Label.grid(row=1, column=1, pady=5)

        newButton = tk.Button(self, text="New Account", command=lambda: self.controller.show_frame("RegPage"))
        newButton.grid(row=2, column=1, ipady=5, ipadx=10)

        or2Label = tk.Label(self, text="or")#, font=tkFont.Font(size=14))
        or2Label.grid(row=3, column=1, pady=5)

        nameLabel = tk.Label(self, text="Name:")
        nameLabel.grid(row=4, column=0, sticky="e")

        nameEntry = tk.Entry(self)
        nameEntry.grid(row=4, column=1, padx=5)

        searchButton = tk.Button(self, text="Search")
        searchButton.grid(row=4, column=2, sticky="w")


