class Person:
    """
    This class is used to instantiate Person objects.
    """
    def __init__(self, name, status):
        self.firstName = name[0]
        self.lastName = name[1]
        self.status = status
