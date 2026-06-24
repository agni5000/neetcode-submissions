class Solution:
    def isPalindrome(self, s: str) -> bool:
        ch = "".join(char.lower() for char in s if char.isalnum())
        rev= ch[::-1]

        if rev == ch:
            return True 
        else:
            return False
