import Tkinter as tk
import tkFont

import LogicController as LC
import DocIDPage
import IdlePage
import RegPage


class GuiHandler(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # First set up the Logic Controller, which each GUI will
        # use to interact with the sheets
        self.lc = LC.LogicController()

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (DocIDPage.DocIDPage, IdlePage.IdlePage, RegPage.RegPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self, lc_in=self.lc)
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

    def busy(self):
        self.config(cursor="watch")
        self.update_idletasks()

    def not_busy(self):
        self.config(cursor="")
        self.update_idletasks()

