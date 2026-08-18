class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        b = []
        c = []
        candidates.sort()
        def bt(i , sum):
            if sum > target:
                return
            if i >= len(candidates):    
                if sum == target:
                    b.append(c.copy())
                return
            c.append(candidates[i])
            bt(i+1, sum+ candidates[i])
            c.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            bt(i + 1, sum)
            
        bt(0,0)
       
        print(b)
        
        return b