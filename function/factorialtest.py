def power(n, i):
    if i == 1:
        return n
    return n*power(n, i-1)


print(power(5, 2))


# 回文
def backnum(s):
    if len(s) < 2:
        return True
    elif s[0] != s[-1]:
        return False
    return backnum(s[1:-1])


print(backnum("123"))
print(backnum("abcba"))
