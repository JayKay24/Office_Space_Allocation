import room

class LivingSpace(room.Room):
    """
    This class is used to initialize LivingSpace objects.
    """
    def __init__(self, name, max_num=4):
        self.name = name
        self.max_num = max_num
