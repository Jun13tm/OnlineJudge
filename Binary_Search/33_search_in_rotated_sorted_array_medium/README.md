# Summary
Difficulty: Medium<br/>
[Link to problem](https://leetcode.com/problems/search-in-rotated-sorted-array/)<br/>
## sol1: 48ms(78%)
比较经典的题，写了binary search和binary search with pivot两个Helper functions，分开handle。依旧是Binary Search比较核心的问题，edge case handling。值得重做
## sol2: 
真的是牛皮的写法，generic BS也可以照着这个改写。不用Recursion也不需要管offset了，直接记录现在这一节nums在array上的位置。
# Topics
- Binary Search
- Edge Case Handling