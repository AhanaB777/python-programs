"""21. Write a Python function that checks whether a passed string is palindrome or not."""
def isPalindrome(s):
    rev_s=s[::-1]
    if rev_s == s:
        print("Palindrome")
    else:
        print("Not a palindrome")
s="racecar"
isPalindrome(s)