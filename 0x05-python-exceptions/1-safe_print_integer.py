#!/usr/bin/python3

def safe_print_integer(value):
    """Prints an integer with "{:d}".format().

    Args:
        value (int): integer to be printed

    Returns:
        If TypeError or ValueError occurs - False.
        if no error - True.
    """
    try:
        print("{:d}".format(value))
