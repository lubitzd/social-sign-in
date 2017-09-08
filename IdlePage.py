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
        self.columnconfigure(0, weight=1)

        scanLabel = tk.Label(self, text="Scan a card", font=tkFont.Font(size=14))
        scanLabel.grid(row=0, column=0)

        noIDButton = tk.Button(self, text="No ID", command=lambda: self.controller.show_frame("RegPage"))
        noIDButton.grid(row=1, column=0, ipady=10, ipadx=10, pady=10, padx=10, sticky="se")
