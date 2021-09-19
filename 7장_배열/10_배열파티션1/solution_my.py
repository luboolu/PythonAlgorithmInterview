from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums) // 2
        nums.sort()
        nums = [str(n) for n in nums]
        nums = "".join(nums)
        split_num = [nums[i:i+2] for i in range(0, len(nums), 2)]

        print(split_num)

        for i in range(n):
            answer += min(int(split_num[i][0]), int(split_num[i][1]))

        return answer

sol = Solution()
print(sol.arrayPairSum([6214, -2290, 2833, -7908]))