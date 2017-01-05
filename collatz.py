# collatz functions


def collatz_steps(num: int) -> int:
    """runs the collatz conjecture on num, returns number of steps"""
    if num == 0:
        return 0
    n = 0
    while num != 1:
        n += 1
        if (num % 2) == aa0:
            num /= 2
        else:
            num = (num * 3) + 1
    return n


def collatz_from_one_to_x(x: int) -> list:
    """returns number of steps of collatz from numbers 1 to x"""
    result = list()
    for num in range(1,x):
        result.append(collatz_steps(num))
    return result
