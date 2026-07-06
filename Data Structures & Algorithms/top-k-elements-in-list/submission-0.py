from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res  ={}
        jo = []
        for mo in nums:
            if( mo not in res):
                res[mo] = res.get(mo , 0) +1
            else:
                res[mo] = res[mo] + 1
        
        sorted_us = sorted(res.items() , key = lambda x: x[1] , reverse = True)
        for i in range (0,k):
            jo.append(sorted_us[i][0])
        return jo
