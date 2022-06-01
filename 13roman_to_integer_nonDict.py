class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        had_special_case = False
        for i in range(len(s)): 
            # print(result)
            if(had_special_case):
                had_special_case = False
                continue
            # Special Case
            if(s[i] == 'I'):
                if(i+1 < (len(s))):
                    if(s[i+1] == 'V'):
                        result += 4
                        had_special_case = True
                        continue
                    if(s[i+1] == 'X'):
                        result += 9
                        had_special_case = True 
                        continue
                result += 1
            
            if(s[i] == 'V'):
                result += 5
                
            # Special Case
            if(s[i] == 'X'):
                if(i+1 < (len(s))):
                    if(s[i+1] == 'L'):
                        result += 40
                        had_special_case = True
                        continue
                    if(s[i+1] == 'C'):
                        result += 90
                        had_special_case = True
                        continue
                result += 10
            
            if(s[i] == 'L'):
                result += 50
                
            # Special Case
            if(s[i] == 'C'):
                if(i+1 < (len(s))):
                    if(s[i+1] == 'D'):
                        result += 400
                        had_special_case = True
                        continue
                    if(s[i+1] == 'M'):
                        result += 900
                        had_special_case = True
                        continue        
                result += 100
            
            if(s[i] == 'D'):
                result += 500
        
            if(s[i] == 'M'):
                result += 1000
        
        return result
            
sl = Solution()

print(sl.romanToInt("CXC"))
