class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        m = len(mat)
        n = len(mat[0])
        result = []
        for d in range(m + n - 1):
            diag = []
            r = 0 if d < n else d - n + 1
            c = d if d < n else n - 1
            while r < m and c >= 0:
                diag.append(mat[r][c])
                r += 1
                c -= 1
            if d % 2 == 0:
                diag.reverse()
            result += diag
        return result
