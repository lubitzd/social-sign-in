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
        self.clubMemberVar = tk.IntVar()
        memberCheckbutton = tk.Checkbutton(membershipFrame, text="Member of Club", \
                            variable=self.clubMemberVar)
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
        rfid_index = self.lc.get_column_index("master", "RFID")
        self.rfidNumVar.set(data[rfid_index])

        # Club member CBox & Member type menu
        member_status_index = self.lc.get_column_index("master", "Member Status")
        self.clubMemberVar.set("member" in data[member_status_index])
        self.memberTypeVar.set(data[member_status_index].replace("member", "").strip())

        # Early sign up CBox
        self.earlyVar.set(self.is_early_bird())

# NEW USERS NOT HANDLED YET (BOTH BUTTON AND SCAN)
# also maybe run the function every keystroke in rcs id
        #early_index = self.lc.get_column_index("early", "")
        
        #self.earlyVar.set()

        # Email list CBox
        email_index = self.lc.get_column_index("master", "On Email List")
        self.emailVar.set("y" in data[email_index])

        # Amount Due
        self.amountDueNumVar.set(self.calulate_amt())


    def is_early_bird(self):
        # First read the early list
        rcs_col_letter = self.lc.get_column_letter("early", "RCS ID")
        name_col_letter = self.lc.get_column_letter("early", "Name")

        rcs_col = self.lc.read_column("early", rcs_col_letter)
        name_col = self.lc.read_column("early", name_col_letter)

        # TODO: go through one by one the rcs ids, if it's N/A look at the name



#        early_row_index = find_row("early", "RCS ID", self.rcsVar.get())
        # If the RCS ID was found in the early list
        # I.e., user is a student, was on master list, signed up early
#        if early_row_index >= 0:
#            return True

        # RCS ID not on early list
#        early_row_index = find_row("early", "Name", self.nameVar.get())
        # If the Name was found in the early list
#        if early_row_index >= 0:
            # I.e., user is not a student, was on master list, signed up early
#            return True


    def calulate_amt(self):
        if self.lc.get_on_dance_sheet() or self.clubMemberVar.get():
            return 0
        if self.earlyVar.get():
            return 2
        return 5


