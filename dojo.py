class Dojo:
    """
    This class accepts a list of offices and living spaces objects and
    initializes Dojo objects.
    """
    def __init__(self, offices, living_spaces):
        self.__offices = offices
        self.__living_spaces = living_spaces

    @property
    def offices(self):
        return len(self.__offices)

    @property
    def living_spaces(self):
        return len(self.__living_spaces)
    
