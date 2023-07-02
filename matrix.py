from typing import Literal, Tuple


def to_linear(x: int, y: int , base: Literal[0, 1], size: int=16) -> int:
    """Converts the row, column coordinates of a LED in a matrix of given size
       to the linear index, either on base 0 or 1.
       Useful for addressing LEDs in a WS281x matrix.
    """
  
    assert(size > 0)
    assert(base <= x < size + base)
    assert(base <= y < size + base)

    if (y + base) % 2:
        return (y - base + 1) * size - (x + 1 - 2 * base)
    else:
        return (y - base) * size + x

def to_matrix(linear: int, base: Literal[0, 1], size: int=16) -> Tuple[int, int]:
    """Converts the linear index of a chain of LEDs to its row, column coordinates.
    """
  
    assert(size > 0)
    assert(base <= linear < size*size + base)

    print(linear)
    y = (linear - base) // size + base
    if (y - base) % 2:
        x = (y + 1 - base) * size - linear + 2 * base - 1
    else:
        x = (linear - base) % size + base


    assert(base <= x < size + base)
    assert(base <= y < size + base)

    return (x, y)
