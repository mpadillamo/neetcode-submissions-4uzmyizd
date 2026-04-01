class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        memo = {}
        memo[amount] = 99999999
        coins.sort(reverse=True)

        def dfs(coins, total, amount, lvl):
            if total in memo and lvl >= memo[total]:
                return
            
            memo[total] = lvl

            if memo[amount] <= lvl + 1:
                return
 
            for el in coins:
                if total + el == amount:
                    memo[amount] = min(memo[amount],lvl+1) # Appending element
                    return

            for el in coins:
                if el + total < amount:
                    dfs(coins, el + total, amount, lvl + 1)

        dfs(coins, 0, amount, 0)
        if memo[amount] == 99999999:
            return -1

        return memo[amount]
