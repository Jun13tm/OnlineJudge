# Overview
- Medium
- [Link to problem](https://leetcode.com/problems/3sum/)

## 61%
将3sum的问题转换为n个2sum问题，改进2sum返回无重复的解。在main里面sort最初的nums，跳过
nums里所有重复的数字。可以这么做是因为这个数字出现的第一次时已经在ret里append了包括这个
数字的所有的triplets。一定要记得sort<br/>
因为是O(n^2)的时间复杂度，可以先sort。</br>

# Topics
- sort
- array
