"""
198. House Robber
Medium

9958

228

Add to List

Share
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""
# SOMEONES SOLUTION FOR ME TO UNDERSTAND DP:
#  slicing nums[:i-1] or any positive interger takes in acount the number of elements should be taken from the
# start eg: nums[:2] will take two elements from the first one in the list whereas nums[:-2] will give all besides the two last elements
# class Solution:
#     def rob(self, nums):
#         print(nums)
#         for i in range(2,len(nums)):
#             print(i, "    printing i \n")
#             print("nums at i is ", nums[i])
#             print("\n nums [ : i-1]    ", nums[:i-1])
#            # print(nums[:1])
#             print("\n max nums .... ", max(nums[:i-1]))
#             nums[i] += max(nums[:i-1])
#             print("\n nums i is max of the previus thing... ", nums[i])

#         return max(nums)

# class Solution:
#     def rob(self, A):
#         print(nums)
#         prev2, prev, cur = 0,0,0
#         for i in A:
#             print("\n previous    ", prev)
#             print(" previous2    ", prev2)
#             print(" cur    ", cur)
#             print("\n i  ", i, " + prev2 ", prev2, " is ", i+prev2)
#             cur = max(prev, i + prev2)
#             prev2 = prev
#             prev = cur
#             print("\n AFTER previous    ", prev)
#             print(" AFTER previous2    ", prev2)
#             print(" AFTER cur    ", cur)
#         return cur

class Solution:
    def rob(self, nums):
        previous_house_max = 0
        pre_previous_house_max = 0
        current_max = 0
        for current_house in nums:
            current_max = max(previous_house_max, current_house + pre_previous_house_max)
            pre_previous_house_max = previous_house_max
            previous_house_max = current_max
        return current_max

# Time Complexity : O(N)
# Space Complexity : O(1), only constant extra space is used.

# class Solution(object):
#     def rob(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         for num in nums:
            


#         return max

# nums = [1,2,3,1]
# nums = [2,7,9,3,1]
nums = [2,1,1,2]
# nums = [1,3,1,3,100]
# nums = [4,1,1,1,1,1,1,4]
# nums = [1,2,1,2,1,2]
sol = Solution()
print(sol.rob(nums))