def is_even(i):
    """
        This function tells if a given number is even or odd
        Input any valid integer
        Return odd/even
        Created by Anubhav
        Last edited 31 December
    """
    if type(i) == int:
        if i%2 == 0:
            return 1
        else:
            return 0
    else:
        return "Invalid value"