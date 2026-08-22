class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = 0
        m = {}
        while x < len(nums):
            res = target - nums[x]
            if res in m:
                return [m[res],x]
            m[nums[x]] = x
            x += 1
        return []