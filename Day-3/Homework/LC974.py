class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count = {0: 1}
        total = 0
        result = 0
        for n in nums:
            total = (total + n) % k
cat > Day-1/Homework/LC2235.py << 'EOF'
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2
