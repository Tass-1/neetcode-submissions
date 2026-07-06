from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for word in strs:
            sorted_w = "".join(sorted(word))
            if( sorted_w not in result):
                result[sorted_w] = []
            result[sorted_w].append(word)
        return list(result.values())
                    