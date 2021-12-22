"""
204. Count Primes
Medium

Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106
"""

class Solution(object):
    def isPrime(self, num):
        prime = False
        if num > 1:
            for i in range(2, int(num**1/2) + 1): # start from 2 because every number is dividable by 1. and range upto num is num-1 because all is dividable itself
                print("i ", i)
                if num % i == 0:
                    # print("num is ", num, " NOT prime when dividied by i ", i)
                    return False
            return True
            # else:
            #     # prime = True
            #     print("prime number is ", num)
            #     return True
        else:
            return False
        # print("num is ", num, " prime ")
        # return prime

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0 
        for num in range(1, n + 1):
            print("num ", num)
            prime = self.isPrime(num)
            if prime and num < n:
                count += 1
        print("primen count ", count)
        return count


sol = Solution()
n = 499979
print(sol.countPrimes(n))
