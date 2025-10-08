'''
Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''

def twoSum(nums, target):
    seen = {}  # dictionary to store number -> index

    for i, num in enumerate(nums):
        complement = target - num  # what number do we need to reach the target?

        if complement in seen:
            return [seen[complement], i]  # found the pair!

        # store the current number with its index
        seen[num] = i

nums = [3, 2, 4]
target = 6
print(twoSum(nums, target))
