from Room.room import Room

class Office(Room):
    """
    This class is used to initialize Office objects.
    """
    def __init__(self, name, max_num=6):
        super().__init__(name)
        self.max_num = max_num
        self.__spaces_left = 6

    @property
    def spaces_left(self):
    	return self.__spaces_left

    @spaces_left.setter
    def spaces_left(self, value):
    	self.__spaces_left = value

    def allocate_space(self):
    	self.spaces_left -= 1
