class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1
        sr = sorted(s1)
        while(r < len(s2)):
            temp = sorted(s2[l:r+1])
            if(temp == sr):
                return True
            else:
                l = l + 1 
                r = r + 1
        return False