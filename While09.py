def main(s):
    """
    A string of numbers is given. Find the sum of all the numbers and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    j=0
    i=0
    while i < len(s):
        j += int(s[i])
        i += 1
    return j
x=main('12')
print(x)