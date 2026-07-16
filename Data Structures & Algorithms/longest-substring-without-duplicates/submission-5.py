class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        isIn = set()
        count = 0
        l = 0
        r = 0
        while(r < len(s)):
            if(s[r] in isIn):
                
                isIn.remove(s[l])
                l = l+1
            else:
                isIn.add(s[r])
                r= r+1
            count = max(count , r - l)
        return count 