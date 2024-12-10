class Solution:
    def isPalindrome(self, s: str) -> bool:
        answer = ''.join(char.lower() for char in s if char.isalnum())
        pal = answer[::-1]
        if (pal == answer):
            return True
        else:
            return False