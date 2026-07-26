class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i==j:
                    continue
                SUM = nums[i]+nums[j]
                if SUM==target:
                    a=[i,j]
                    return a
                