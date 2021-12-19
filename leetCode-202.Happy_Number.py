"""
202. Happy Number
Easy

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly 
in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1

"""
# SOMEONES SOLUTION TO EXPLORE AND UNDERSTAND.
#  class Solution:
#     def isHappy(self, n: int) -> bool:
        
#         if n == 1 or n == 7:
#             return "true"
        
#         elif n>1 and n<10:
#             return n == 1
        
#         else:
#             s = n
        
#             while s > 9:
#                 temp = s
#                 s = 0
#                 while temp > 0:
#                     mod = temp % 10
#                     temp = temp // 10
#                     s += mod**2
                    
#             return s == 1 or s == 7


# Success
# Details 
# Runtime: 20 ms, faster than 79.07% of Python online submissions for Happy Number.
# Memory Usage: 13.6 MB, less than 13.06% of Python online submissions for Happy Number.
# THIS SOLUTION IS WITH LIST BUT BETTER TO USE DIC - BETTER USE OF MEMORY BUT NOT MUCH...

# Success
# Details 
# Runtime: 20 ms, faster than 79.07% of Python online submissions for Happy Number.
# Memory Usage: 13.3 MB, less than 67.98% of Python online submissions for Happy Number.

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        seen_dict = {} 
        result = 0
        num = n
        i = 1
        while True:# True: #i < 20: #not happy:#result != 1:
            
            # result_list  = [ int(digit)**2 for digit in str(num)] 
            result = sum(int(digit)**2 for digit in str(num))
            i += 1
            # print(result_list)
            # print(result)
            num = result
            if result == 1:
                # print(result)
                return True
            if result not in seen_dict:
                seen_dict[result] = 1
            else:
                # print(" it is already in seen ", result, " this is the list ", seen_list)
                return False
            


sol = Solution()
# n = 19
# n = 2
# n = 7
n = 3
# print(sol.isHappy(n))
sol.isHappy(n)