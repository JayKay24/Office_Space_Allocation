from Person.person import Person

class Fellow(Person):
    """
    This class is used to initialize Fellow objects.
    """
    def __init__(self, fname, lname, status):
        super().__init__(fname, lname, status)
        self.living_space_name = ""

    def assign_living_space(self, name):
    	self.living_space_name = name