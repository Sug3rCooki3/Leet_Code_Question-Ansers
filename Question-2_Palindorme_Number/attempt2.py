def reverse(i):
    rev = 0
    while i > 0:
        digit = i % 10
        rev = rev * 10 + digit
        i //= 10
    return rev

def palindrome(i):
    if i < 0:
        return False
    return i == reverse(i)

test2 = [121, -121, 10, -101]
print([palindrome(i) for i in test2])