class QeBaseClass:
    """
    Base class with a method to get non-callable attributes.

    Attributes:
        None

    Methods:
        getattr(): Retrieves non-callable attributes of the class.
    """

    @classmethod
    def getattr(cls) -> dict:
        """
        Retrieves non-callable attributes of the class.

        Returns:
            dict: A dictionary containing attribute names as keys and their values.

        Example:
            >>> class SomeClass(QeBaseClass):
                    ITEMS: List[Tuple[int, int]] = [(10,35), (20,50)]
            >>> print(SomeClass.getattr())
            {'ITEMS': [(10, 35), (20, 50)]}
        """
        return {
            attr: getattr(cls, attr)
            for attr in dir(cls)
            if not callable(getattr(cls, attr)) and not attr.startswith("__")
        }
