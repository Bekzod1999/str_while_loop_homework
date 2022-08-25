import string
def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    j=0
    i=0
    t = string.ascii_lowercase
    while i < len(s):
        k=0
        while k < len(t):
            if s[i] == t[k]:
                j +=1
            k += 1
        i+=1
    return j
x=main('gsfUftsLHGygsf')
print(x)