import Tkinter as tk
import tkFont

class SocialSignInApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (DocIDPage, IdlePage, RegPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("DocIDPage")


    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()



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
        
        instructionsLabel = tk.Label(self, text="[How to get Doc IDs]")
        instructionsLabel.grid(row=0, column=0, columnspan=2)

        masterLabel = tk.Label(self, text="Master ID:")
        masterLabel.grid(row=1, column=0)
        danceLabel = tk.Label(self, text="Dance ID:")
        danceLabel.grid(row=2, column=0)
        earlyLabel = tk.Label(self, text="Early ID:")
        earlyLabel.grid(row=3, column=0)

        masterEntry = tk.Entry(self, width=45)
        masterEntry.grid(row=1, column=1, padx=5)
        danceEntry = tk.Entry(self, width=45)
        danceEntry.grid(row=2, column=1, padx=5)
        earlyEntry = tk.Entry(self, width=45)
        earlyEntry.grid(row=3, column=1, padx=5)
        
        goButton = tk.Button(self, text="Go", command=lambda: self.controller.show_frame("IdlePage"))
        goButton.grid(row=4, column=0, columnspan=2)


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


class RegPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.createRegWidgets()

    def createRegWidgets(self):
        nameEntry = tk.Entry(self)
        nameEntry.grid(row=0, column=0, padx=5, sticky="sw")
        rcsEntry = tk.Entry(self)
        rcsEntry.grid(row=1, column=0, padx=5, sticky="nw")

        rfidLabel = tk.Label(self, text="RFID #:")
        rfidLabel.grid(row=2, column=0, padx=5, sticky="w")

        membershipFrame = tk.Frame(self, borderwidth=1, relief=tk.GROOVE)
        membershipFrame.grid(row=0, rowspan=2, column=1, columnspan=2, pady=5)
        memberCheckbutton = tk.Checkbutton(membershipFrame, text="Member of Club")
        memberCheckbutton.grid()
        self.memberTypeVar = tk.StringVar()
        memberType = tk.OptionMenu(membershipFrame, self.memberTypeVar, "Student", "Community", "Former")
        memberType.grid()

        earlyCheckbutton = tk.Checkbutton(self, text="Signed Up Early")
        earlyCheckbutton.grid(row=2, column=1, columnspan=2, sticky="w")

        emailCheckbutton = tk.Checkbutton(self, text="On Email List")
        emailCheckbutton.grid(row=3, column=1, columnspan=2, sticky="w")

        amountDueLabel = tk.Label(self, text="Amount Due: $3", font=tkFont.Font(size=12))
        amountDueLabel.grid(row=4, column=0)

        cancelButton = tk.Button(self, text="Cancel", background="#EB5757")
        cancelButton.grid(row=4, column=1, pady=10, sticky="se")
        submitButton = tk.Button(self, text="Submit", background="#6FCF97")
        submitButton.grid(row=4, column=2, pady=10, sticky="se")

        
