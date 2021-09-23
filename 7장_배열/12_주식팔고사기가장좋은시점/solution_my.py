from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #한번의 거래로(매수 1번, 매도 1) 낼 수 있는 최대 이익을 return번
        #최소일 때 사서, 최대일 때 팔아야 함(but, index(최소) < index(최대))

        if len(prices) == 1:
            return 0

        profit = []
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                profit.append(prices[j] - prices[i])

        return max(profit)


sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
print(sol.maxProfit([2, 1]))