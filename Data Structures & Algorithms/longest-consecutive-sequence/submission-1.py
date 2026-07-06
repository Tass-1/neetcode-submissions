class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        hi = set(nums)
        li = list(hi)
        ki = sorted(li)
        store = []
        p= 0
        count= 0
        for i in range(len(ki)):
            if( ki[i]+1 == ki[(i+1)%len(ki)]):
                p = 1
                count = count +1
            else:
                p=0
                store.append(count)
                count = 0
        return max(store)+1