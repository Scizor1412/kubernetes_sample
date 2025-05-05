# Given an integer array nums and an integer target, return the indices of the two numbers such that they add up to target.
 
def get_substract(nums, target):
    result_set = set()
    for index, value in enumerate(nums):
        substract = target - value
        if substract in nums:
            result_set.add(tuple(sorted((index, nums.index(substract)))))
    return result_set
        
nums = [2, 7, 5, 4]
target = 9
# Output: [0, 1]

get_substract(nums, target)
