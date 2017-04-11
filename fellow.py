import person

class Fellow(person.Person):
    """
    This class is used to initialize Fellow objects.
    """
    def __init__(self, fname, lname, status):
        super().__init__(fname, lname, status)
        self.opt_in = False
