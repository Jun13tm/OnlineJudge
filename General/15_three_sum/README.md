# Summary
[Link](https://leetcode.com/problems/3sum/)<br/>
##1st Attempt: 992ms(49.0%); 18MB(9%)<br/>
将3sum的问题转换为n个2sum问题，改进2sum返回无重复的解。在main里面sort最初的nums，跳过
nums里所有重复的数字。可以这么做是因为这个数字出现的第一次时已经在ret里append了包括这个
数字的所有的triplets。<br/>
因为是O(n^2)的时间复杂度，可以先sort。</br>
##2st Attempt:
# Topics
- Hash Table
- sorting