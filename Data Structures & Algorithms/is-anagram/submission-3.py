class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicty = {}
        dicte = {}
        if( len(s) != len(t)):
            return False
        
        for i in range (0, len(s)):
            dicty[s[i]] = dicty.get(s[i] , 0) +1
            dicte[t[i]] = dicte.get(t[i] , 0) +1
        if(dicty == dicte):
            return True
        return False