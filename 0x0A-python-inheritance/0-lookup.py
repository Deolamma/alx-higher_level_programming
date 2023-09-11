"""
Printing a list object containing the list of available
attributes and methods of an object
"""


def lookup(obj):
    """
        Getting The Attributes & Methods of An Object

        Args:
            obj: Object in which the attributes and methods is to be gotten
                 Obj can be the name of a user-defined or builtin class

        Returns:
            Returns a list object of the passed in class as argument
    """

    return dir(obj)
