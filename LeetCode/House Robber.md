# House Robber I
## Problem

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

## Solution

This is a DP problem, the minimum subproblem can be modeled as follow:
```
OPT[j] = Max{OPT[j-2]+nums[j], OPT[j-1]}   j>2
         Max{nums[0], nums[1]}             j=2
         nums[0]                           j=1
```

* Code v1.0:
```
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        if not nums:
            return 0
        if len(nums)<3:
            return max(nums)
        s = [0 for i in range(len(nums)+2)]
        s[0] = 0
        s[1] = 0
        for i in range(2, len(nums)+2):
            s[i] = max(s[i-2]+nums[i-2], s[i-1])
        return s[-1]
```
        
To be simple we can just use `last` and `now` to keep track. 
* Note: 
In `last, now = now, max(last+i, now)`, the `last` in the `max` case is the original `last`, not the version after `last = now`.

* Code v2.0:
```
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        
        for i in nums: 
            last = now
            now = max(last + i, now)
                
        return now
```
