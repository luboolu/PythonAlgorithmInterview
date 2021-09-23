from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for n in nums:
            #앞에서부터 오름차순으로 페어를 만들어서 합 계산
            pair.append(n)
            if len(pair) == 2:
                sum += min(pair)
                pair = []

        return sum

sol = Solution()
print(sol.arrayPairSum([6214, -2290, 2833, -7908]))
print(sol.arrayPairSum([1,4,3,2]))