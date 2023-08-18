# Given an array of integers and an integer target, return indices of the two numbers such that they add up to target.
# 'nums': list of integers
# 'target': integer representing the sum 
# '-> List[int]': function will return a list of integers (the indices of the numbers that satisfy condition.
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    prevMap = {} # val : index

    for i, n in enumerate(nums):
      diff = target - n
      if diff in prevMap:
        return [prevMap[diff], i]
      prevMap[n] = i
    return
