from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        print(height)
        ##i - a / i / i + a
        ## i - a <= i < i + a 인 경우를 찾아야함
        ##이런 경우를 찾는다면 answer += a

        left, right = 0, len(height) - 1
        while not left == right:
            if height[left]

sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))