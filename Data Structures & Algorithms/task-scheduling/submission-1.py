class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        min = 0
        k = {}
        p = []
        for ch in tasks:
            k[ch] = k.get(ch , 0)+1
        m = len(tasks)
        mf = max(k.values())
        count = list(k.values()).count(mf)
        min = (mf-1)*(n+1)+count
       
        print(mf)
        print(count)

        

        print(k)
        return max(min,m)