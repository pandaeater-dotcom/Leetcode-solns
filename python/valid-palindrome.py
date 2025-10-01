class Solution:
    def isPalindrome(self, s: str) -> bool:
        modified = ''.join([char.lower() for char in s if char.isalnum()])
        return modified == modified[::-1]
