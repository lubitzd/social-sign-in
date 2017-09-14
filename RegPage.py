import Tkinter as tk
import tkFont

class RegPage(tk.Frame):
    def __init__(self, parent, controller, lc_in):
        tk.Frame.__init__(self, parent)
        self.lc = lc_in
        self.controller = controller
        self.createRegWidgets()

    def createRegWidgets(self):
        nameLabel = tk.Label(self, text="Name:")
        nameLabel.grid(row=0, column=0, sticky="se")
        # Name
        self.nameVar = tk.StringVar()
        nameEntry = tk.Entry(self, textvariable=self.nameVar)
        nameEntry.grid(row=0, column=1, columnspan=2, padx=5, sticky="sw")

        rcsLabel = tk.Label(self, text="RCS ID/Email:")
        rcsLabel.grid(row=1, column=0, sticky="ne")
        # RCS (or email)
        self.rcsVar = tk.StringVar()
        rcsEntry = tk.Entry(self, textvariable=self.rcsVar)
        rcsEntry.grid(row=1, column=1, columnspan=2, padx=5, sticky="nw")

        rfidLabel = tk.Label(self, text="RFID #:")
        rfidLabel.grid(row=2, column=0, padx=5, sticky="e")
        # RFID Num
        self.rfidNumVar = tk.StringVar()
        rfidNumLabel = tk.Label(self, textvariable=self.rfidNumVar)
        rfidNumLabel.grid(row=2, column=1, sticky="w")

        membershipFrame = tk.Frame(self, borderwidth=1, relief=tk.GROOVE)
        membershipFrame.grid(row=0, rowspan=2, column=3, columnspan=2, pady=5)
        # Club Member
        self.clubMemberVar = tk.StringVar()
        memberCheckbutton = tk.Checkbutton(membershipFrame, text="Member of Club", \
                            variable=self.clubMemberVar, onvalue="member", offvalue="")
        memberCheckbutton.grid()
        # Member Type
        self.memberTypeVar = tk.StringVar()
        memberType = tk.OptionMenu(membershipFrame, self.memberTypeVar, "Student", "Community", "Former")
        memberType.grid()

        # Early
        self.earlyVar = tk.IntVar()
        earlyCheckbutton = tk.Checkbutton(self, text="Signed Up Early", variable=self.earlyVar)
        earlyCheckbutton.grid(row=2, column=3, columnspan=2, sticky="w")

        # Email
        self.emailVar = tk.IntVar()
        emailCheckbutton = tk.Checkbutton(self, text="On Email List", variable=self.emailVar)
        emailCheckbutton.grid(row=3, column=3, columnspan=2, sticky="w")

        amountDueLabel = tk.Label(self, text="Amount Due: $", font=tkFont.Font(size=12))
        amountDueLabel.grid(row=4, column=1)
        # Amount Due Num
        self.amountDueNumVar = tk.IntVar()
        amountDueNumLabel = tk.Label(self, textvariable=self.amountDueNumVar, font=tkFont.Font(size=12))
        amountDueNumLabel.grid(row=4, column=2, sticky="w")

        cancelButton = tk.Button(self, text="Cancel", background="#EB5757", \
                        command=self.cancelButtonCallback)
        cancelButton.grid(row=4, column=3, pady=10, sticky="se")
        submitButton = tk.Button(self, text="Submit", background="#6FCF97", \
                        command=self.submitButtonCallback)
        submitButton.grid(row=4, column=4, pady=10, sticky="se")



    def cancelButtonCallback(self):
        self.controller.show_frame("IdlePage")


    def submitButtonCallback(self):
        # Write
        return


    def populate(self):
        master_row = self.lc.get_current_row()
        calc_amt = self.lc.get_calculate_amt()

        # Read the master doc
        data = self.lc.read_row("master", master_row)
        self.lc.inflate_list(data, self.lc.get_headers_length("master"), "")
        if __debug__:
            print "populating reg page with " + str(data)

        # If we're not looking at a blank row
        #if len(data) > 0:
        # Name field   
        name_index = self.lc.get_column_index("master", "Name")
        self.nameVar.set(data[name_index])




