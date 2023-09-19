# complex_id_generator.pyi

def complex_id_generator(char_len: int = 6) -> str:
    """
    Generate a complex ID.

    Parameters:
        char_len (int, optional): The length of the generated ID. Default is 6.

    Returns:
        str: A randomly generated string consisting of alphanumeric characters.

    This function generates a complex ID composed of uppercase and lowercase letters
    along with digits. The length of the generated ID is determined by the `char_len`
    parameter.

    Example:
        >>> complex_id_generator()
        'kP3hR7'
        >>> complex_id_generator(8)
        '4FwS7eZq'
    """
    ...
