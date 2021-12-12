"""
189. Rotate Array
Medium

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different 
ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

# Success
# Details 
# Runtime: 184 ms, faster than 84.28% of Python online submissions for Rotate Array.
# Memory Usage: 25.1 MB, less than 39.86% of Python online submissions for Rotate Array.

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if 0 > k > 10**5 or 1 > len(nums) > 10**5:
            return

        if k >= len(nums):
            quotient, remainder = divmod(k, len(nums))
            print("remainder is " , remainder)
            k = remainder
        # this solution takes the k (ither reduced or original depending on previous condition - equal or larger k than len(nums))
        # and here slicing is used instead of for loop to insert item by item with pop and instert as it takes
        # a lot of run time. So the k number of elements from the end are put to the first part of the array and 
        # the beginning without the k number of elements from the end are added to the new first part of array.
        nums[:] = nums[len(nums) - k:] + nums[0 : len(nums) - k]
        print(nums)



# THIS SOLUTION PASSES ONLY 38/39 TESTS!! RUN TIME ERROR...
# class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         if 0 > k > 10**5 or 1 > len(nums) > 10**5:
#             return

#         reduced_k = k

#         if k >= len(nums):
#             quotient, remainder = divmod(k, len(nums))
#             print("remainder is " , remainder)
#             reduced_k = remainder

#         print(reduced_k)

#         for i in range(reduced_k):
#             popped = nums.pop()
#             #print("popped", popped)
#             nums.insert(0, popped)
#             #print(nums)

#         # print(nums)
        

nums = [1,2,3,4,5,6,7]

k = 3
sol = Solution()
sol.rotate(nums, k)