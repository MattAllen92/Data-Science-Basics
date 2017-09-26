from math import sqrt

def find_next_square(sq):
    if sqrt(sq) % 1 == 0:
        sq += 1
        while sqrt(sq) % 1 != 0:
            sq += 1
        return sq
    else:
        # Return the next square if sq is a square, -1 otherwise
        return -1