import person

class Fellow(person.Person):
    """
    This class is used to initialize Fellow objects.
    """
    def __init__(self, fname, lname, status):
        super().__init__(fname, lname, status)
        self.opt_in = False

    def assign_living_space(self, name):
    	self.living_space_name = name