import room

class Office(room.Room):
    """
    This class is used to initialize Office objects.
    """
    def __init__(self, name, max_num=6):
        self.name = name
        self.max_num = max_num
