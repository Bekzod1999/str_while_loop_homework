def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd numbers.
    Args:
        s: str
    Returns:
        int: return answer
    """
    j=0
    i=0
    while i < len(s):
        if int(s[i]) % 2:
            j += int(s[i])
        i += 1
    return j
x=main('98421')
print(x)