from Person.person import Person

class Staff(Person):
    """
    This class initializes Staff objects.
    """
    def __init__(self, name, fname, status):
        super().__init__(name, fname, status)
        
