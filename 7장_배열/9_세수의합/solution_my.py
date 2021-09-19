from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        #nums.sort()
        for i, a in enumerate(nums):
            tmp_answer = [a]
            for j in range(i + 1, len(nums)):
                for k in range(i + 1, len(nums)):
                    tmp_answer.append(nums[k])

                    if len(tmp_answer) == 3:
                        print(tmp_answer)
                        if sum(tmp_answer) == 0:
                            answer.append(tmp_answer)
                        break
                tmp_answer.clear()

        return answer


sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
