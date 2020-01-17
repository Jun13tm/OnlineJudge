# Summary
Difficulty: Easy<br/>
[Link to problem](https://leetcode.com/problems/search-insert-position/)<br/>
## sol1: 64ms(23%)
Binary Search的基础题，用了Resursion。有两个要点需要注意：<br/>
1. 二分的时候要把midpoint放入后半array中，应对len(nums) = 2的情况。
2. Stop condition，target小于last element或等于last element，都return 0(即last element所在的位置)
# Topics
- Binary Search