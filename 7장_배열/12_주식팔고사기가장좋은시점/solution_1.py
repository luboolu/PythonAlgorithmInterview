from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #min_price = sys.maxsize ##에러를 방지하기 위해 시스템의 최댓값으로 설정
        min_price = prices[0]
        profit = 0


        for p in prices:
            min_price = min(min_price, p)
            profit = max(p - min_price, profit)

        return profit

sol = Solution()
print(sol.maxProfit([3,3,5,0,0,3,1,4]))