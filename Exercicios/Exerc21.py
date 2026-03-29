def checkPalindrome(inputString):
    return inputString == inputString[::-1]

print(checkPalindrome("aabaa"))
print(checkPalindrome("abac"))
print(checkPalindrome("a"))