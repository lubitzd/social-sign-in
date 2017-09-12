import SheetManager as SM


class LogicController:
    #def __init__(self):
    #    return

    def init_sheets(self, master, dance, early):
        self.master_doc = SM.SheetManager(master)
        self.dance_doc = SM.SheetManager(dance)
        self.early_doc = SM.SheetManager(early)



