# Problem
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

# Solution

Idea: Set two pointers, one at the left side of the array and one at the right side of array. And move one of them closer at each time, then we can traverse
all the possible area in `O(n)` 

Keeps the maximum area and finally return them.

Code:
```
# Only keeps the max area is enough
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        pointL = 0
        pointR = len(height)-1
        maxArea = (len(height)-1)*min(height[pointL],height[pointR])
        while pointL < pointR:
            maxArea = max(maxArea, (pointR-pointL)*min(height[pointL],height[pointR]))
            if height[pointL] < height[pointR]:  # 每次只移左指针或右指针的秘诀
                pointL += 1
            else:
                pointR -= 1
        return maxArea
```
