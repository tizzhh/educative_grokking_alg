def max_profit(prices: list[int]) -> int:
    buy, sell = 0, 1
    max_profit = 0
    while sell < len(prices):
        if prices[buy] < prices[sell]:
            cur_profit = prices[sell] - prices[buy]
            max_profit = cur_profit if cur_profit > max_profit else max_profit
        else:
            buy = sell
        sell += 1

    return max_profit


print(max_profit([7, 1, 5, 3, 6, 4]))
