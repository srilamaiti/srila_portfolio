#https://leetcode.com/problems/largest-number/?envType=daily-question&envId=2024-09-18
from functools import cmp_to_key

def custom_compare(a, b):
    # Compare two concatenated results
    if a + b > b + a:
        return -1
    else:
        return 1

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        x = [str(e) for e in sorted(nums, reverse=True)]
        x.sort(key = cmp_to_key(custom_compare))
        if int(''.join(x)) == 0:
            return '0'
        else:
            return ''.join(x)
