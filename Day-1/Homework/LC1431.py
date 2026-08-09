class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        highest = max(candies)
        result = []
        for c in candies:
            result.append(c + extraCandies >= highest)
        return result
