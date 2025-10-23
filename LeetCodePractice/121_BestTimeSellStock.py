'''
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

示例 1：
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
'''
'''
若在前 i 天选择买入，若想达到最高利润，则一定选择价格最低的交易日买入。
考虑根据此贪心思想，遍历价格列表 prices 并执行两步：
由于初始值 i=0 ，为了序号对应，本文设从第 0 天开始；
更新前 i 天的最低价格，即最低买入成本 cost；
更新前 i 天的最高利润 profit ，
即选择「前 i−1 天最高利润 profit 」和「第 i 天卖出的最高利润 price - cost 」中的最大值 ；
'''
'''
知识点： print 使用f-string 或者使用format函数都可以
'''
def maxProfit(prices):
    min_cost = 0xffffffe
    max_profit = 0
    for i in prices:
        min_cost = min(min_cost, i)
        max_profit = max(max_profit, i - min_cost)
        print(f"i={i}, cost = {min_cost}, profit = {max_profit}")
    return max_profit

def test_profit():
    prices = [7, 1, 5, 3, 6, 4]
    result = maxProfit(prices)
    print("max profit = {}".format(result))
test_profit()