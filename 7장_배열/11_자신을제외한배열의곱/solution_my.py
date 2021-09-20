from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        product_list = []
        for i, n in enumerate(nums):
            product_list.append(nums[:i] + nums[i + 1:])

        for p in product_list:
            pro = 1
            pro = [pro * i for i in p]





sol = Solution()
print(sol.productExceptSelf([1,2,3,4]))