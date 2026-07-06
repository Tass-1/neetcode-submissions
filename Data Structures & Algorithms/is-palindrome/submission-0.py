class Solution:
    def isPalindrome(self, s: str) -> bool:
        le = 0
        ri = len(s)-1
        while le < ri:
            if not s[le].isalnum():
                le = le+1
                continue
            elif not s[ri].isalnum():
                ri = ri -1
                continue
            if( s[le].lower() != s[ri].lower()):
                return False
            le = le +1
            ri = ri -1
        return True
