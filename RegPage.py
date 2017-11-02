import Tkinter as tk
import tkFont

class RegPage(tk.Frame):
    def __init__(self, parent, controller, lc_in):
        tk.Frame.__init__(self, parent)
        self.lc = lc_in
        self.controller = controller
        self.createRegWidgets()

    def createRegWidgets(self):
        nameLabel = tk.Label(self, text="Name:", font=self.controller.customFont)
        nameLabel.grid(row=0, column=0, sticky="se")
        # Name
        self.nameVar = tk.StringVar()
        nameEntry = tk.Entry(self, textvariable=self.nameVar, font=self.controller.customFont)
        self.nameVar.trace("w", self.nameUpdatedCallback)
        nameEntry.grid(row=0, column=1, columnspan=2, padx=5, sticky="sw")

        rcsLabel = tk.Label(self, text="RCS ID/Email:", font=self.controller.customFont)
        rcsLabel.grid(row=1, column=0, sticky="ne")
        # RCS (or email)
        self.rcsVar = tk.StringVar()
        rcsEntry = tk.Entry(self, textvariable=self.rcsVar, font=self.controller.customFont)
        self.rcsVar.trace("w", self.rcsUpdatedCallback)
        rcsEntry.grid(row=1, column=1, columnspan=2, padx=5, sticky="nw")

        rfidEntry = tk.Label(self, text="RFID #:", font=self.controller.customFont)
        rfidEntry.grid(row=2, column=0, padx=5, sticky="e")
        # RFID Num
        self.rfidNumVar = tk.StringVar()

        rfidNumLabel = tk.Entry(self, textvariable=self.rfidNumVar, font=self.controller.customFont)
        rfidNumLabel.grid(row=2, column=1, sticky="w")

        membershipFrame = tk.Frame(self, borderwidth=1, relief=tk.GROOVE)
        membershipFrame.grid(row=0, rowspan=2, column=3, columnspan=2, pady=5)
        # Club Member
        self.clubMemberVar = tk.IntVar()
        self.memberCheckbutton = tk.Checkbutton(membershipFrame, text="Member of Club", \
                            variable=self.clubMemberVar, command=self.memberBoxCallback, \
                            font=self.controller.customFont)
        self.memberCheckbutton.grid()
        # Member Type
        self.memberTypeVar = tk.StringVar()
        options = ["Student", "Community", "Former"]
        self.memberTypeMenu = tk.OptionMenu(membershipFrame, self.memberTypeVar, \
                                   *options, command=self.memberTypeCallback)
        self.memberTypeMenu['menu'].config(font=self.controller.customFont)
        self.memberTypeMenu.grid()

        # Early
        self.earlyVar = tk.IntVar()
        earlyCheckbutton = tk.Checkbutton(self, text="Signed Up Early", \
                                        variable=self.earlyVar, command=self.earlyBoxCallback, \
                                        font=self.controller.customFont)
        earlyCheckbutton.grid(row=2, column=3, columnspan=2, sticky="w")

        # Email
        self.emailVar = tk.IntVar()
        emailCheckbutton = tk.Checkbutton(self, text="On Email List", variable=self.emailVar, \
                                        font=self.controller.customFont)
        emailCheckbutton.grid(row=3, column=3, columnspan=2, sticky="w")

        amountDueLabel = tk.Label(self, text="Amount Due: $", font=self.controller.customFontLarge)
        amountDueLabel.grid(row=4, column=1, sticky="w")
        # Amount Due Num
        self.amountDueNumVar = tk.IntVar()
        amountDueNumLabel = tk.Label(self, textvariable=self.amountDueNumVar, font=self.controller.customFontLarge)
        amountDueNumLabel.grid(row=4, column=1, sticky="e", padx=20)

        cancelButton = tk.Button(self, text="Cancel", background="#EB5757", \
                        command=self.cancelButtonCallback, font=self.controller.customFont)
        cancelButton.grid(row=4, column=3, pady=10, sticky="se")
        submitButton = tk.Button(self, text="Submit", background="#6FCF97", \
                        command=self.submitButtonCallback, font=self.controller.customFont)
        submitButton.grid(row=4, column=4, pady=10, sticky="se")


    def rcsUpdatedCallback(self, *args):
        self.earlyVar.set(self.is_early_bird())
        self.amountDueNumVar.set(self.calulate_amt())

    def nameUpdatedCallback(self, *args):
        if self.rcsVar.get() == "":
            self.earlyVar.set(self.is_early_bird())
            self.amountDueNumVar.set(self.calulate_amt())

    def memberBoxCallback(self):
        # If club member is deselected while the type is Former, switch away from Former
        if self.clubMemberVar.get() == 0 and self.memberTypeVar.get() == "Former":
            self.memberTypeVar.set("Community")
        # Every time button is toggled, recalc
        self.amountDueNumVar.set(self.calulate_amt())

    def memberTypeCallback(self, member_type):
        if member_type == "Former":
            self.memberCheckbutton.flash()
            self.memberCheckbutton.select()
            self.amountDueNumVar.set(self.calulate_amt())

    # The Operator can override the automatic early checker
    def earlyBoxCallback(self):
        self.amountDueNumVar.set(self.calulate_amt())
        

    def cancelButtonCallback(self):
        self.controller.show_frame("IdlePage")


    # Write data in GUI to master and dance sheets
    def submitButtonCallback(self):
        self.controller.busy()

        master_row = self.lc.get_current_row()

        # Read the master doc
        data = self.lc.read_row("master", master_row)
        self.lc.inflate_list(data, self.lc.get_headers_length("master"), "")

        # Calculate total amt spent  
        total_amt_index = self.lc.get_column_index("master", "Total amount payed")
        if data[total_amt_index] == "":
            total_amt = 0
        else:
            total_amt = int(data[total_amt_index])
        total_amt += int(self.amountDueNumVar.get())

        # Calculate socials attended
        socials_index = self.lc.get_column_index("master", "Socials Attended")
        if data[socials_index] == "":
            socials_att = 0
        else:
            socials_att = int(data[socials_index])
        if not self.lc.get_on_dance_sheet():
            socials_att += 1

        # Set up data to export to master
        member_status = self.memberTypeVar.get() + (" member" if self.clubMemberVar.get() else "")
        data = [[self.rfidNumVar.get(), self.nameVar.get(), self.rcsVar.get(), member_status, \
                "y" if self.emailVar.get() else "n", socials_att, total_amt]]

        self.lc.write_row("master", self.lc.get_current_row(), data)

        # First find the row in the dance sheet to save to if they're already on it
        if self.lc.get_on_dance_sheet():
            # If they have an RFID, search for that
            if not self.rfidNumVar.get() == "":
                dance_row = self.lc.find_row("dance", "RFID", self.rfidNumVar.get())
            else:
                # Otherwise search by name
                dance_row = self.lc.find_row("dance", "Name", self.nameVar.get())
        else:
            # otherwise find the net blank row
            dance_row = self.lc.find_open_row("dance")
            
        # Set up data to export to dance
        data = [[self.rfidNumVar.get(), self.nameVar.get(), member_status, \
                 "y" if self.emailVar.get() else "n", "y" if self.earlyVar.get() else "n", \
                 int(self.amountDueNumVar.get())]]
        self.lc.write_row("dance", dance_row, data)

        self.controller.not_busy()
        self.controller.show_frame("IdlePage")
        


    def populate(self):
        self.controller.busy()

        master_row = self.lc.get_current_row()

        # Read the master doc
        data = self.lc.read_row("master", master_row)
        self.lc.inflate_list(data, self.lc.get_headers_length("master"), "")
        if __debug__:
            print "populating reg page with " + str(data)

        # Name field   
        name_index = self.lc.get_column_index("master", "Name")
        self.nameVar.set(data[name_index])

        # RCS (or email) field
        rcs_index = self.lc.get_column_index("master", "RCS ID")
        self.rcsVar.set(data[rcs_index])

        # RFID num
        if len(self.lc.get_RFID()) > 0:
            self.rfidNumVar.set(self.lc.get_RFID())
        else:
            rfid_index = self.lc.get_column_index("master", "RFID")
            self.rfidNumVar.set(data[rfid_index])

        # Club member CBox
        member_status_index = self.lc.get_column_index("master", "Member Status")
        self.clubMemberVar.set("member" in data[member_status_index])
        # Member type menu
        memberType = data[member_status_index].replace("member", "").strip()
        self.memberTypeVar.set(memberType if len(memberType) else
                               self.memberTypeMenu["menu"].entrycget(0, "label"))

        # Early sign up CBox
        self.earlyVar.set(self.is_early_bird())

        # Email list CBox
        email_index = self.lc.get_column_index("master", "On Email List")
        self.emailVar.set("y" in data[email_index])

        # Amount Due
        self.amountDueNumVar.set(self.calulate_amt())

        self.controller.not_busy()


    def is_early_bird(self):
        # There shouldn't be any blank entries,
        #  as both questions are required on the form.
        # Go through the rcs ids, if it's N/A look at the name
        for i in range(1, len(self.lc.early_rcs_col)):
            # If it's an RCS ID
            if not self.lc.early_rcs_col[i].lower() == "n/a":
                # Compare the ids
                if self.lc.early_rcs_col[i].lower() == self.rcsVar.get().lower():
                    return True
            else:
                # Compare the names
                if self.lc.early_name_col[i].lower() == self.nameVar.get().lower():
                    return True

        return False


    def calulate_amt(self):
        if self.lc.get_on_dance_sheet() or self.clubMemberVar.get():
            return 0
        if self.earlyVar.get():
            return 2
        return 5


