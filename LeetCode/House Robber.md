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


# House Robber II
## Problem
Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

## Solution
This problem can be break up into simpler problem to make use of sloutions in House Robber I

Main idea: Break the circle at a house not being robbed

Which is:

- Not rob house i, then break the circle from I, use solution form House Robber I to solve the problem
- Not rob house i+1,....

Assume we choose to not rob house i, then we are free to choose rob i+1 or not.

Note:
```
nums[len(nums) != 1:] 
eg1. nums = [1,2,3,4,5]
nums[len(nums) != 1:]  = [2,3,4,5]
nums[:-1] = [1,2,3,4]
eg2: nums = [1]
nums[len(nums) != 1:]  = [1]
```

Code:
```
class Solution:
    def rob(self, nums):
        def rob_helper(nums):
            last, now = 0, 0
            for i in nums:
                last, now = now, max(last+i, now)
            return now
        return max(rob_helper(nums[len(nums) != 1:]), rob_helper(nums[:-1]))
```
