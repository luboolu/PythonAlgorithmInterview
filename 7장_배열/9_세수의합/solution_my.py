from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums)):
                for k in range(i + 2, len(nums)):
                    if i != j and i != k and j != k and i < j and j < k:
                        if (nums[i] + nums[j] + nums[k]) == 0:
                            if [nums[i], nums[j], nums[k]] not in answer:
                                answer.append([nums[i], nums[j], nums[k]])

        return answer


sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
