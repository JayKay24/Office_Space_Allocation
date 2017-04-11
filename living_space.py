import room

class LivingSpace(room.Room):
    """
    This class is used to initialize LivingSpace objects.
    """
    def __init__(self, name, max_num=4):
        self.name = name
        self.max_num = max_num
        self.__spaces_left = 4

    @property
    def spaces_left(self):
    	return __spaces_left

    def allocate_space(self):
        self.__spaces_left -= 1
