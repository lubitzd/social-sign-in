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

    def set_current_row(self, row_in):
        self.current_row = row_in

    def find_open_row(self, sheet):
        # Read the first column and get its length
        rows = len(self.docs[sheet].read("A:A"))
        # The row after the last one is open
        if __debug__:
            print "DEBUG: Found open slot in " + sheet + " at " + str(rows + 1)
        return rows + 1

    def find_row(self, sheet, heading, label):
        # Do the actual searching, return row index
        doc = self.docs[sheet]
        col = doc.get_column_letter(heading)
        # the list comp here 'unpacks' each singleton list
        # to make a list of vals of the column
        column = [x[0] for x in doc.read(col + ":" + col)]
        try:
            # Sheets are 1-indexed
            index = column.index(label) + 1
        except ValueError:
            index = -1

        if __debug__:
            print "DEBUG: fininding " + label + " in " + str(column) + " at " + str(index)

        return index


    def search(self, heading, label):
        # First search the dance sheet
        # Then the master sheet
        # Also read early sheet
        self.find_row("master", heading, label)


