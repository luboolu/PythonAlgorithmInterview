from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            #짝수번째 값의 합 계산
            if i % 2 == 0:
                sum += n

        return sum

sol = Solution()
print(sol.arrayPairSum([6214, -2290, 2833, -7908]))
print(sol.arrayPairSum([1,4,3,2]))