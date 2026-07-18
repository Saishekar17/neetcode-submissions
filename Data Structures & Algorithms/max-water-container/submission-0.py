class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #we use i, j so become O(n2)

        maxAns = 0
        n = len(heights)
        for i in range(n):
            for j in range(i + 1, n):
                width = j - i
                height = min(heights[i], heights[j])
                maxAns = max(maxAns, width*height)

        return maxAns
        