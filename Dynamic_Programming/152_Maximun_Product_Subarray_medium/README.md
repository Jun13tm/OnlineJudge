# Summary
Difficulty: Medium<br/>
[Link to problem](https://leetcode.com/problems/maximum-product-subarray/)<br/>
## sol1: 64(74%), memory 14MB
记录每个Index的max and min（when include nums[i]注意max和min的时候3个值都要比较。再额外记录一个overall_max，每次和这个位置的max比较一下大小。
# Topics
- Dynamic Programming 
- Subarray