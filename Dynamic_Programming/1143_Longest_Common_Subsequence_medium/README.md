# Summary
Difficulty: Medium<br/>
[Link to problem](https://leetcode.com/problems/longest-common-subsequence/)<br/>
## sol1: 1980ms(3%), memory 640MB
算法的方法是，相同字母直接划掉+1，然后Recursion。不同字母就binary划分下去recursion。用memorization减少重复的计算量。Worst case: O(2^mn)，及完全没有相同的字母。
## sol2: 484ms(31%), memory 35.4MB
Table Filling。在每个格子注意如果字母相同，append 1+list[i-1][j-1]。如果字母不同，就继承up or left cell里面大的那个。一共填m * n个格子，所以是O(mn)。</br>
用Table Filling的时候，在外侧加一圈0作为padding，处理Edge Case。但是要注意row和col的index要+ or - 1，很容易出错。需要想清楚。
## sol2: 
# Topics
- Dynamic Programming 
- Sub-Sequence