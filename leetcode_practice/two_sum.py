#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums, target):
        pos_list = []
        for i in range(len(nums)):
            if (target - nums[i]) in nums[i+1:]:
                pos_list.append(i)
                pos_list.append(nums.index(target - nums[i], i+1))
                break
        return pos_list#[i, nums.index(target - nums[i], i+1)]