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


    def set_calculate_amt(self, calc_in):
        self.calculate_amt = calc_in

    def get_calculate_amt(self):
        return self.calculate_amt


    def set_current_row(self, row_in):
        self.current_row = row_in

    def get_current_row(self):
        return self.current_row

    
    def get_column_index(self, sheet, label):
        return self.docs[sheet].get_column_index(label)


    def read_row(self, sheet, index):
        data = self.docs[sheet].read(str(index) + ":" + str(index))
        if len(data) > 0:
            # The [0] unpacks the list from the list
            return data[0]
        return data


    def find_open_row(self, sheet):
        # Read the first column and get its length
        rows = len(self.docs[sheet].read("A:A"))
        # The row after the last one is open
        if __debug__:
            print "DEBUG: Found open slot in " + sheet + " at " + str(rows + 1)
        return rows + 1


    # Do the actual searching, return row index or -1 if not found
    def find_row(self, sheet, heading, label):
        doc = self.docs[sheet]
        col = doc.get_column_letter(heading)
        # the list comp here 'unpacks' each one-element list
        # to make a list of vals of the column
        # it also converts to lower case for easier matching
        column = [x[0].lower() for x in doc.read(col + ":" + col)]
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



