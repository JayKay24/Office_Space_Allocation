import room

class Office(room.Room):
    """
    This class is used to initialize Office objects.
    """
    def __init__(self, max_num=4):
        self.max_num = max_num
