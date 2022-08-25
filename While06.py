import string
def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """

    j=0
    i=0
    t = string.ascii_letters
    while i < len(s):
        k=0
        while k < len(t):
            if s[i] == t[k]:
                j +=1
            k += 1
        i+=1
    return j
x=main('HyuO123')
print(x)