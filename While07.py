# import string
def main(s):
    """
    A string of numbers is given. Find how many even numbers there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
#     j=0
#     i=0
#     t = string.digits
#     while i < len(s):
#         k=0
#         while k < len(t):
#             if s[i] == t[k]:
#                 if int(s[i]) % 2 == 0:
#                     j += 1
#             k += 1
#         i+=1
#     return j
# x=main('123456')
# print(x)


    j=0
    i=0
    while i < len(s):
        if int(s[i]) % 2 == 0:
            j += 1
        i += 1
    return j
x=main('123456')
print(x)