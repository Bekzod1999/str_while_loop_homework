def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    k=0
    i=0

    while i < len(s):
        if s[i].isalpha():
            k += 1
        i += 1
    return k
x=main('ssd1f25')
print(x)