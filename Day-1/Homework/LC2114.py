class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        best = 0
        for s in sentences:
            words = len(s.split())
            if words > best:
                best = words
        return best
