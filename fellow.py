import person

class Fellow(person.Person):
    """
    This class is used to initialize Fellow objects.
    """
    def __init__(self, name, status):
        super().__init__(name, status)
        self.opt_in = False
