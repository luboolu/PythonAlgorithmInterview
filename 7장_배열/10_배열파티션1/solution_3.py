from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

sol = Solution()
print(sol.arrayPairSum([6214, -2290, 2833, -7908]))
print(sol.arrayPairSum([1,4,3,2]))