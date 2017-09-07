import Tkinter as tk


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
        for F in (DocIDPage, IdlePage): # and RegPage
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
        instructionsLabel = tk.Label(self, text="[How to get Doc IDs]")
        instructionsLabel.grid(row=0, column=0, columnspan=2)

        masterLabel = tk.Label(self, text="Master ID:")
        masterLabel.grid(row=1, column=0)
        danceLabel = tk.Label(self, text="Dance ID:")
        danceLabel.grid(row=2, column=0)
        earlyLabel = tk.Label(self, text="Early ID:")
        earlyLabel.grid(row=3, column=0)

        masterEntry = tk.Entry(self, width=45)
        masterEntry.grid(row=1, column=1)
        danceEntry = tk.Entry(self, width=45)
        danceEntry.grid(row=2, column=1)
        earlyEntry = tk.Entry(self, width=45)
        earlyEntry.grid(row=3, column=1)
        
        goButton = tk.Button(self, text="Go", command=lambda: self.controller.show_frame("IdlePage"))
        goButton.grid(row=4, column=0, columnspan=2)


class IdlePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.createIdleWidgets()

    def createIdleWidgets(self):
        nameEntry = tk.Entry(self)
        nameEntry.grid(row=0, column=0)




        
