"""
Logic:
We want to set a pointer to the start and end of the list and iterate through the list. We break whenever the left and right pointer meet.
We will use a result variable to store our result, and update it through each iteration of the loop. 

To calculate the area of a rectangle we use base x height. Height is given to us. One note about height, we want to use the minimum of the two heights we currently have. This is because if our heights are not the same, water will spill.
We can calculate "base" by subtracting our left pointer from our right pointer

At every iteration we will calculate the area and compare it with the area we already have saved. We want to save the highest one so we can use the max function.

At every iteration we must also adjust our pointers. Since we always want the higher of the two pointers, we will always adjust the pointer with the lower height, 
for example if pointer L, height[l], is 8 and pointer r, height[r] is 6, then we would adjust the right pointer. This is because our left pointer is already maximizing our area, and potentially lowering it would only lower our area.

At the end we can just return res, since it is updated throughout the loop.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        res = 0

        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            print(res)
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
        return res
