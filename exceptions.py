class LengthNotFiveAndAlphabets(Exception):
    """raised when input consists of anything else than alphabets"""
    pass

class InvalidWord(Exception):
    """raised when word is not in dictionary"""
    pass

class SameInput(Exception):
    """raised when same input is give twice"""
    pass