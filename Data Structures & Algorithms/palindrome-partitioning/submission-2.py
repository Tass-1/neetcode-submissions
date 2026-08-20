class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPa(p , l, r):
            while l < r:
                if p[l] != p[r]:
                    return False
                l += 1
                r -= 1
            return True
        res = []
        c = []
        def bt(i):
            if i >= len(s):
                res.append(c.copy())
                return
            
            for j in range(i,len(s)):
                if isPa(s, i, j):
                    c.append(s[i:j+1])
                    bt(j+1)
                    c.pop()
        bt(0)
        return res
