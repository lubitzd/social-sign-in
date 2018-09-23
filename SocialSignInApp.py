import Tkinter as tk
import GuiHandler


def on_closing():
    app.ser_thread.stop()
    app.destroy()


if __name__ == "__main__":
    app = GuiHandler.GuiHandler()
    app.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()
