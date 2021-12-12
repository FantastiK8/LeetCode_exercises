"""
172. Factorial Trailing Zeroes
Medium

Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

 

Example 1:

Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Example 3:

Input: n = 0
Output: 0
 

Constraints:

0 <= n <= 104

###############
My notes:
1.OPTION
existing but not leetCode accepted math.
Syntax: math.factorial(x)
EXAMPLE: 

import math 
    
x = 5
    
# returning the factorial
print ("The factorial of 5 is : ", end ="") 
print (math.factorial(x))

####
2.OPTION
Recursively


def recur_factorial(n):
if n == 1:
   return n
elif n < 1:
   return ("NA")
else:
   return n*recur_factorial(n-1)
print (recur_factorial(int(num)))

OR EXAMPLE 2

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)


####
3.OPTION
for loop
Using a For Loop
We can use a for loop to iterate through number 1 till the designated number and 
keep multiplying at each step. In the below program we ask the user to enter the 
number and convert the input to an integer before using it in the loop. This way 
we ensure we get positive integers in the calculation.

n = 5
factorial = 1
if int(n) >= 1:
for i in range (1,int(n)+1):
   factorial = factorial * i
print("Factorail of ",n , " is : ",factorial)

OR EXAMPLE 2:

def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact


"""
# NOTE very bad results... NEEDS OPTIMISATION IN THE FUTURE!!!
# Success
# Details 
# Runtime: 4512 ms, faster than 5.75% of Python online submissions for Factorial Trailing Zeroes.
# Memory Usage: 20.9 MB, less than 5.36% of Python online submissions for Factorial Trailing Zeroes.

class Solution(object):
    def factorial(self, n):
        if n == 1:
            return 1
        elif n < 1:
            return
        else:
            return n * self.factorial(n - 1)

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        fact = self.factorial(n)
        fact = str(fact)
        count = 0
        for num in fact[:: -1]:
          #  if int(num) == 0: # working in VSC but not in LeetCode!!!
            if num == '0':
                count += 1
            else:
                break

        return count 
        

       #nr_of_zeros = sum(1 if num == '0' and not found else found = True for num in fact[::-1])
# n = 3
n = 7
# n = 0
sol = Solution()
print(sol.trailingZeroes(n))
