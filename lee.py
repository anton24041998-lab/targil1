#   Amid Saleh — 23:10
# Repository for the first question on leetcode
#
# Two Sum
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
# Constraints:
#
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
#
import random
nums: list= []
answer_key=[]
_target = random.randint(-109,109)
print(_target)
for i in range(30):
    nums.append(random.randint(2,104))
print(nums)
for num in nums:
    for num2 in nums:
        if num + num2 == _target and nums.index(num) != nums.index(num2):
            answer_key.append(nums.index(num))
            answer_key.append(nums.index(num2))
            print(answer_key)
            break
    if len(answer_key) == 2:
        break
else:
    print('no answer')