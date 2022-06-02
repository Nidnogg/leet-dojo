from __future__ import annotations

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        longest_prefix = ""
        
        # needs to run sorting algorithm on array first.
        for word, idx in enumerate(strs):
            for word_to_compare in strs[word+1:]:
                print("word - {} vs word_to_compare {}".format(strs[word], word_to_compare))
                
                
sl = Solution()
sl.longestCommonPrefix(["hey", "hello"])