from tkinter import Frame

from gui.WindowBuilder import WindowBuilder


class MainWindow(Frame):

    def __init__(self, master, contexts):
        self.__master = master
        self.__builder = WindowBuilder(contexts)
        Frame.__init__(self, master, height=self.__builder.get_height(), width=self.__builder.get_width())
        self.__center_on_screen()
        #self.__add_components()

    def __center_on_screen(self):

        # Gets the requested values of the height and widht.
        window_width = self.__master.winfo_reqwidth()
        window_height = self.__master.winfo_reqheight()
        print("Width", window_width, "Height", window_height)

        # Gets both half the screen width/height and window width/height
        position_right = int(self.__master.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(self.__master.winfo_screenheight() / 3 - window_height / 3)

        # Positions the window in the center of the page.
        self.__master.geometry("+{}+{}".format(position_right, position_down))

