class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        roman_int_dict = {'I': 1, 'V': 5 , 'X': 10 , 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        const_dict = {'IV':4 , 'IX':9 , 'XL':40 , 'XC':90 , 'CD':400 , 'CM': 900}
        had_special_case = False

        for i in range(len(s)):
            if(had_special_case): 
                had_special_case = False
                continue
            if(i + 1 < len(s) and s[i] + s[i+1] in const_dict):
                result += const_dict[str(s[i] + s[i+1])]
                had_special_case = True
            else:
                result += roman_int_dict[str(s[i])]
       
        return result
            
sl = Solution()

print(sl.romanToInt("CXC"))
