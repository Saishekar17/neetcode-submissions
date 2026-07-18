class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #this become optimal i.e O(n)
        left,right = 0, len(heights) - 1
        maxAns = 0
        while left < right:
            width = right - left 
            height = min(heights[left], heights[right])
            maxAns = max(maxAns, width*height)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxAns 

        