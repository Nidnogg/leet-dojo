from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash_set = {}
        for idx in nums:
            hash_set[idx] = hash_set.get(idx, 0) + 1
            
        def get_key_from_value(d, val):
            keys = [k for k, v in d.items() if v == val]
            if keys:
                return keys[0]
            return None
        print(hash_set)
        i = 2
        while(get_key_from_value(hash_set, i) == None):
            i += 1
        return get_key_from_value(hash_set, i)        