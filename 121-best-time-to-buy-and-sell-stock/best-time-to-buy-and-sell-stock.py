# 전략 : 앞에서부터 돌아가면서 제일 작은 변수 와 profit을 계산한다
# 앞에서부터 min 보다 작으면 얘를 min에 넣고 아니면 min을 뺀 값을 profit에 저장한다
# min보다 큰 숫자들은 profit에만 값을 저장하는 것에 의미가 있고 다시 볼 필요가 없음


class Solution:
    def maxProfit(self,prices):
        if len(prices) < 2 or not prices : return 0
        minimum = float('inf')
        profit = 0
        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                im = prices[i] - minimum
                if(im > profit):
                    profit = im
        return profit
