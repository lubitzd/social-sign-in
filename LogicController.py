import SheetManager as SM


class LogicController:
    #def __init__(self):
    #    return

    def init_sheets(self, master, dance, early):
        self.master_doc = SM.SheetManager(master)
        self.dance_doc = SM.SheetManager(dance)
        self.early_doc = SM.SheetManager(early)
        self.docs = {"master" : self.master_doc, "dance" : self.dance_doc, \
                      "early" : self.early_doc}
        # Download the early sheet, as it won't change
        rcs_col_letter = self.get_column_letter("early", "RCS ID")
        name_col_letter = self.get_column_letter("early", "Name")

        self.early_rcs_col = self.read_column("early", rcs_col_letter)
        self.early_name_col = self.read_column("early", name_col_letter)

        # Expand both lists to the size of the other one
        # They can't get shorter, so both get set to the size of the longer one
        self.inflate_list(self.early_rcs_col, len(self.early_name_col), "")
        self.inflate_list(self.early_name_col, len(self.early_rcs_col), "")


    # Gets set when leaving the Idle Page (on either search or new account)
    # Checks for user's [name or RFID, whatever the search term was] on dance sheet
    def set_on_dance_sheet(self, on_dance_sheet_in):
        self.on_dance_sheet = on_dance_sheet_in

    def get_on_dance_sheet(self):
        return self.on_dance_sheet


    def get_RFID(self):
        return self.RFID

    def set_RFID(self, rfid):
        self.RFID = rfid


    def set_current_row(self, row_in):
        self.current_row = row_in

    def get_current_row(self):
        return self.current_row

    
    def get_column_index(self, sheet, label):
        return self.docs[sheet].get_column_index(label)

    def get_column_letter(self, sheet, label):
        return self.docs[sheet].get_column_letter(label)

    def get_headers_length(self, sheet):
        return self.docs[sheet].get_headers_length()


    def inflate_list(self, lst, length, val):
        needed = length - len(lst)
        extras = [val] * needed
        lst += extras


    def read_row(self, sheet, row):
        data = self.docs[sheet].read(str(row) + ":" + str(row))
        if len(data) > 0:
            # The [0] unpacks the list from the list
            return data[0]
        return data

    def write_row(self, sheet, row, data):
        self.docs[sheet].write(str(row) + ":" + str(row), data)

    def read_column(self, sheet, col):
        # If you can figure out what this does, good for you
        return [x[0] if len(x) else x for x in self.docs[sheet].read(col + ":" + col)]


    def find_open_row(self, sheet):
        # Read the name & rcsID columns and get the length
        rows = len(self.docs[sheet].read(self.docs[sheet].get_column_letter("Name") \
                               + ":" + self.docs[sheet].get_column_letter("RCS ID")))
        # The row after the last one is open
        if __debug__:
            print "DEBUG: Found open slot in " + sheet + " at " + str(rows + 1)
        return rows + 1


    # Do the actual searching, return row index or -1 if not found
    def find_row(self, sheet, heading, label):
        doc = self.docs[sheet]
        col = doc.get_column_letter(heading)
        # The list comp here 'unpacks' each one-element list
        #  to make a list of vals of the column
        # It also converts to lower case for easier matching
        if __debug__:
            print "column is " + str(doc.read(col + ":" + col)) + " from " + sheet
        column = [x[0].lower() if len(x) else "" for x in doc.read(col + ":" + col)]
        try:
            # Sheets are 1-indexed
            index = column.index(label.lower()) + 1
        except ValueError:
            index = -1

        if __debug__:
            print "DEBUG: fininding " + label.lower() + " in " \
                    + sheet + "'s " + str(column) + " at " + str(index)

        return index


    # Looks for the specified credential in the database
    # Returns tuple: (already_logged, index_in_master/-1 if not found)
    def search(self, heading, label):
        # First check the master sheet
        master_row = self.find_row("master", heading, label)
        # If there's no match
        if master_row == -1:
            return (False, -1)
        
        # User exists in master, now check dance sheet
        dance_row = self.find_row("dance", heading, label)
        # If they've already been logged in the dance sheet
        if dance_row >= 0:
            return (True, master_row)

        # Else add a new user
        return (False, master_row)



