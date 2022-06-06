class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        else:   
            return (''.join(sorted(s)) == ''.join(sorted(t)))
        