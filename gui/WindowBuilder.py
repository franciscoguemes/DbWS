from tkinter import Button


class WindowBuilder:
    DEFAULT_HEIGHT = 200
    DEFAULT_WIDTH = 200

    def __init__(self, main_window, contexts):
        self.__main_window = main_window
        self.__contexts = contexts
        self.__num = len(contexts)
        self.__rows, self.__columns = self.__calculate_geometry()

    def __calculate_geometry(self):

        if self.__num == 0:
            # TODO: Raise an exception here!!! Don't you have any project?
            pass

        if self.__num > 15:
            # TODO: Raise an exception here!!! Too many projects!!!
            pass

        geometry = {
            1: (1, 1),
            2: (1, 2),
            3: (1, 3),
            4: (2, 2),
            5: (2, 3),
            6: (2, 3),
            7: (3, 3),
            8: (3, 3),
            9: (3, 3),
            10: (4, 3),
            11: (4, 3),
            12: (4, 3),
            13: (4, 4),
            14: (4, 4),
            15: (4, 4),
            16: (4, 4),
        }
        return geometry[self.__num][0], geometry[self.__num][1];

    def get_height(self):
        return self.__rows * WindowBuilder.DEFAULT_HEIGHT

    def get_width(self):
        return self.__columns * WindowBuilder.DEFAULT_WIDTH

    def get_columns(self):
        return self.__columns

    def get_rows(self):
        return self.__rows

    # def add_button(self, frame, row, column):
    #
    #     context = self.__contexts[self.__get_context_index(row, column)]
    #
    #     button = Button(frame, text=context.get_name(), command=lambda: context.switch(self.__main_window))
    #     button.grid(row=row, column=column, pady=20, padx=20)

    def get_context(self, row, column):
        return self.__contexts[self.__get_context_index(row, column)]

    def __get_context_index(self, row, column):
        return row * self.get_columns() + column