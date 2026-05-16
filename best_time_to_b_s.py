class Solution:
    def maxProfit(self, prices):

        min_price = float('inf')
        max_profit = 0

        for price in prices:

            # update minimum buying price
            if price < min_price:
                min_price = price

            # calculate profit
            profit = price - min_price

            # update maximum profit
            if profit > max_profit:
                max_profit = profit

        return max_profit
