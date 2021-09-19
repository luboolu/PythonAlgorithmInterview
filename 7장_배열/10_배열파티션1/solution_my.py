from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums) // 2
        nums.sort()

        split_num = [nums[i:i + 2] for i in range(0, len(nums), 2)]

        for i in range(len(nums) // 2):
            answer += min(split_num[i][0], split_num[i][1])

        return answer

sol = Solution()
print(sol.arrayPairSum([6214, -2290, 2833, -7908]))
print(sol.arrayPairSum([1,4,3,2]))