import room

class LivingSpace(room.Room):
    """
    This class is used to initialize LivingSpace objects.
    """
    def __init__(self, max_num=4):
        self.max_num = max_num
