import tkinter
from tkinter import Frame, Label, TOP, BOTTOM, CENTER, LEFT, Button

from gui.WindowBuilder import WindowBuilder


class MainWindow(Frame):

    def __init__(self, master, contexts):
        self.__master = master
        self.__builder = WindowBuilder(self, contexts)
        Frame.__init__(self, master, height=self.__builder.get_height(), width=self.__builder.get_width())
        self.__center_on_screen()
        self.__add_components()

    def __center_on_screen(self):

        # Gets the requested values of the height and widht.
        window_width = self.__master.winfo_reqwidth()
        window_height = self.__master.winfo_reqheight()
        # print("Width", window_width, "Height", window_height)

        # Gets both half the screen width/height and window width/height
        position_right = int(self.__master.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(self.__master.winfo_screenheight() / 3 - window_height / 3)

        # Positions the window in the center of the page.
        self.__master.geometry("+{}+{}".format(position_right, position_down))

    def __add_components(self):
        top_frame = Frame(self)
        label = Label(top_frame, text="¿What do you want to do today?")
        label.pack(side=LEFT)
        top_frame.pack()

        bottom_frame = Frame(self)
        rows = self.__builder.get_rows()
        columns = self.__builder.get_columns()

        counter = 0
        for row in range(rows):
            for column in range(columns):
                if counter < self.__builder.get_contexts_len():
                    button = self.__add_button(bottom_frame, row, column)
                    counter+=1
                else:
                    break
        bottom_frame.pack()

    def __add_button(self, frame, row, column):

        context = self.__builder.get_context(row, column)

        button = Button(frame, text=context.get_name(), command=lambda: self.__switch_context(context))
        button.grid(row=row, column=column, pady=20, padx=20)
        return button

    def __switch_context(self, context):
        print(f"Executing context: \"{context.get_name()}\"")
        context.switch()

        # Close the window...
        self.destroy()
        self.__master.update()
        self.__master.destroy()
