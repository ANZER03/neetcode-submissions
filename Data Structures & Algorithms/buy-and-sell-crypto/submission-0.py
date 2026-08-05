class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) <= 1 :
            return 0

        r, l = 0 ,  0 
        max_profit = float("-inf")
        # print(max_profit)

        while r <= len(prices) - 1 :

            curr = prices[r] - prices[l]
            print(curr)

            max_profit = max (max_profit, curr )



            if  curr <= 0 :
                l = r
            r += 1

        return max_profit
