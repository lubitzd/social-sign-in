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

        scanLabel = tk.Label(self, text="Scan a card", font=self.controller.customFontLarge)
        scanLabel.grid(row=0, column=1)

        or1Label = tk.Label(self, text="or", font=self.controller.customFont)
        or1Label.grid(row=1, column=1, pady=5)

        newButton = tk.Button(self, text="New Account", command=self.newAccountCallback, \
                            font=self.controller.customFont)
        newButton.grid(row=2, column=1, ipady=5, ipadx=10)

        or2Label = tk.Label(self, text="or", font=self.controller.customFont)
        or2Label.grid(row=3, column=1, pady=5)

        nameLabel = tk.Label(self, text="Name:", font=self.controller.customFont)
        nameLabel.grid(row=4, column=0, sticky="e")

        self.nameVar = tk.StringVar()
        nameEntry = tk.Entry(self, textvariable=self.nameVar, font=self.controller.customFont)
        nameEntry.grid(row=4, column=1, padx=5)

        searchButton = tk.Button(self, text="Search", command=self.searchByNameCallback, \
                                font=self.controller.customFont)
        searchButton.grid(row=4, column=2, sticky="w")

        self.errorLabelVar = tk.StringVar()
        self.errorLabel = tk.Label(self, textvariable=self.errorLabelVar, fg="#EB1717", \
                                   font=self.controller.customFont)
        self.errorLabel.grid(row=5, column=1, pady=2, sticky="n")
        self.hideErrorLabel()


    def hideErrorLabel(self):
        self.errorLabelVar.set("")

    def showErrorLabel(self):
        self.errorLabelVar.set("No match found")
        self.errorLabel.after(6000, self.hideErrorLabel)


    # Find the next open row in the master sheet
    def newAccountCallback(self):
        # Stop listening for RFID cards
        self.controller.ser.set_listen(False)
        self.controller.busy()
        row = self.lc.find_open_row("master")
        self.lc.set_on_dance_sheet(False)
        self.lc.set_current_row(row)
        self.controller.not_busy()
        self.controller.show_frame("RegPage")


    def searchByNameCallback(self):
        # Stop listening for RFID cards
        self.controller.ser.set_listen(False)
        self.controller.busy()
        (already_logged, index) = self.lc.search("Name", self.nameVar.get())

        # If name not found
        if index == -1:
            # Display error, then do nothing
            self.showErrorLabel()
            self.controller.not_busy()
            # Start listening for RFID cards again
            self.controller.ser.set_listen(True)
            return

        # If we've already seen this person
        self.lc.set_on_dance_sheet(already_logged)

        self.lc.set_current_row(index)
        
        self.controller.not_busy()
        self.controller.show_frame("RegPage")


    def populate(self):
        self.nameVar.set("")
        self.hideErrorLabel()
        self.after(10, self.controller.ser.read_serial)

