from keyword import kwlist


def main(s):
    """
    A variable of type str is given. Find how many numbers it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    k = 0
    i = 0
    while i < len(s):
        if s[i].isdigit():
            k += 1
        i += 1
    return k
x=main('bekzod1999nuhamm5adiyev')
print(x)