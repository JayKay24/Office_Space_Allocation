class Person:
    """
    This class is used to instantiate Person objects.
    """
    def __init__(self, fname, lname, status):
        self.firstName = fname
        self.lastName = lname
        self.status = status

    def assign_office_space(self, office_name):
    	self.office_name = office_name