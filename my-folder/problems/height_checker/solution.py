class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        result = []
        for i in range(len(heights)):
            if expected[i] != heights[i]:
                result.append(i)
        return len(result)