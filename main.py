from typing import List

def twoSum(self, nums: List[int], target) -> List[int]:
    ans: List[int] = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if(nums[i] + nums[j] == target):
                ans.extend([i, j])
    return ans