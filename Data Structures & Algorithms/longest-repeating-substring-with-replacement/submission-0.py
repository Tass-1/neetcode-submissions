class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = 1
        isIn = {}
        c = k
        l = 0
        ml = 0
        maxf = 0
        for r in range(len(s)):
            isIn[s[r]] = isIn.get(s[r] , 0) + 1
            maxf = max(maxf , isIn[s[r]])
            if( (r-l+1) - maxf > k):
                isIn[s[l]] = isIn[s[l]] -1
                l = l + 1
            
            ml = max( ml, r-l+1)
        return ml