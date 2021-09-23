from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #한번의 거래로(매수 1번, 매도 1) 낼 수 있는 최대 이익을 return번
        #최소일 때 사서, 최대일 때 팔아야 함(but, index(최소) < index(최대))
        #최대인 지점과 profit이 최대인 지점이 항상 일치하는 것은 아니다.-틀림
        if len(prices) == 1:
            return 0

        profit = [0]
        re_prices = prices[:0:-1]
        max_day = len(prices) - re_prices.index(max(re_prices)) - 1

        for i in range(len(prices)):
            if i < max_day:
                profit.append(prices[max_day] - prices[i])

        return max(profit)

sol = Solution()
# print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
# print(sol.maxProfit([2, 4, 1]))
# print(sol.maxProfit([7, 6, 4, 3, 1]))
# print(sol.maxProfit([3, 2, 6, 5, 0, 3]))
#print(sol.maxProfit([2, 1, 2, 0, 1, 2]))
#print(sol.maxProfit([0,1,2,3,4,5]))
print(sol.maxProfit([3,3,5,0,0,3,1,4]))