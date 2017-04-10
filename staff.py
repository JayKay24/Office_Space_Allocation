import person

class Staff(person.Person):
    """
    This class initializes Staff objects.
    """
    def __init__(self, name, status):
        super().__init__(name, status)
        
