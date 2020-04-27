class Plateau(object):
    WIDTH = 0
    HEIGHT = 0

    def __init__(self, width, height, min_width=0, min_height=0):
        self.width = width
        self.height = height
        self.WIDTH = min_width
        self.HEIGHT = min_height

    def move_available(self, position):
        """

        :param Position position:
        :return:
        """
        return self.WIDTH <= position.x <= self.width and self.HEIGHT <= position.y <= self.height
