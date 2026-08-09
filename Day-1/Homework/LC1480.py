class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        total = 0
        result = []
        for n in nums:
            total += n
            result.append(total)
        return result
