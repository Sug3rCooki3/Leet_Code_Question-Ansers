def isPalindrome(i):
    if i < 0:
        return False
    else:
        return str(i) == str(i)[::-1]

test1 = [121, -121, 10, -101]
    
print([isPalindrome(i) for i in test1])