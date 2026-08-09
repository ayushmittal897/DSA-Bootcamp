class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        best = 0
        for account in accounts:
            wealth = sum(account)
            if wealth > best:
                best = wealth
        return best
