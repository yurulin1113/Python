def factorials(n):
    result = n
    for i in range(1, n):
        result *= i
    return result


# print(factorials(5))

def factorials2(n):
    if n == 1:
        return 1
    return n*factorials2(n-1)


print(factorials2(5))
