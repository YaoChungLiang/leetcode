# my solution using linear approach, it's wrong
class Solution1:
    def coinChange(self, coins, amount):
        coins.sort()
        tmp_res = None
        OgAmount = amount
        while coins:
            amount = OgAmount
            total_num = 0
            for val in coins[::-1]:
                num = amount//val
                amount -= num*val
                total_num += num
                if amount == 0:
                    break
            if amount != 0:
                tmp_res = -1
            else:
                return total_num
            if tmp_res == -1:
                coins.pop()
        return -1
    
class Solution:
    def coinChange(self, coins,amount):
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin] +1)
        return dp[amount] if dp[amount] != float('inf') else -1
        

if __name__ == "__main__":
    # coins = [186,419,83,408]
    # amount = 6249
    coins = [5,2,1]
    amount = 11
    sol = Solution()
    print(sol.coinChange(coins,amount))