


class WindowBuilder:
    DEFAULT_HEIGHT = 200
    DEFAULT_WIDTH = 200

    def __init__(self, contexts):
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

