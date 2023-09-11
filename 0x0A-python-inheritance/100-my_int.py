"""
MyInt inherits from the int class
MyInt acts as a rebel and overrides the __eq__ method
"""


class MyInt(int):
    """
    Creating a Rebel MyInt class
    This class does the reverse of the __eq__ method
    i.e. It overrides the __eq__ method
    For instance:
        my_int = MyInt(3)
        print(my_i == 3) # Should return FALSE
    """

    def __init__(self, value):
        """
        Constructor for myInt class
        Inherits from the int class

        Args:
            value: value is the int value passed as argument to the class

        Raises:
            TypeError: This is raised if the argument passed is not int
        """

        if not isinstance(value, int):
            raise TypeError("Value has to be of type int")

        super().__init__()
        self.value = value

    def __eq__(self, comparator):
        """
        Overrides the default __eq__ method of int class

        Args:
            comparator: an int object

        Returns:
            returns False if comparator is equal to MyInt instance
        """

        if isinstance(comparator, int):
            if self.value == comparator:
                return False
        elif isinstance(comparator, MyInt):
            if self.value == comparator.value:
                return False
        return False

    def __ne__(self, comparator):
        """
        Overrides the default __ne__ method of int class

        Args:
            comparator: an int object

        Returns:
            returns True if comparator is not equal to MyInt instance
        """
        return not self.__eq__(comparator)
