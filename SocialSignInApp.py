import Tkinter as tk
import GuiHandler


def on_closing():
    app.ser_thread.stop()
    app.destroy()


if __name__ == "__main__":
    app = GuiHandler.GuiHandler()
    app.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()
    

# master  1BVedAhtD37Ocy4CGXiJPQ7Rrc8Va5G0akSqQVXFqS_0
# dance   1f1XkRPCYjhU604NQoyxYRSk2kGxTr25rYCYz4pgcD-o
# early   
