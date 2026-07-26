class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")[::-1] 
        s = ''.join(ch for ch in s.lower() if ch.isalnum())[::-1]
        srev = ''.join(ch for ch in s.lower() if ch.isalnum())[::-1]        
        if s == srev:
            return True
        return False