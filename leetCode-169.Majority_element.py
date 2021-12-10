"""
169. Majority Element
Easy

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

# Success
# Details 
# Runtime: 132 ms, faster than 90.56% of Python online submissions for Majority Element.
# Memory Usage: 14.8 MB, less than 48.38% of Python online submissions for Majority Element.


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lenght_nums = len(nums)
        majority_min = len(nums)/2
        dict = {}


        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                 dict[num] = 1
        
        for num in dict:
            if dict[num] > majority_min:
                return num




nums = [2,2,1,1,1,2,2]
nums = [3,2,3]
sol = Solution()
print(sol.majorityElement(nums))