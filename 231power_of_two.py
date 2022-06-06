import math
from decimal import Decimal
# Should work, but float truncates small values. Borked with 536870912
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        print(Decimal(math.log(n,2))
        print(math.log(n,2))
#         if(Decimal(math.log(n,2)) - int(math.log(n,2)) == 0):
#             return True
#         else:
#             return False