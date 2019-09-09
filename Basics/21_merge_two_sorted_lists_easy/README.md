# Summary
Difficulty: Easy<br/>
[Link to problem](https://leetcode.com/problems/longest-common-prefix/)<br/>
## sol1: 48ms(18%)
这个方法用了Vertical Scanning (从第1，2，3..位数字开始比较)。同理还有Horizontal Scanning，即先比较两个str，得出结果后用该结果之后和下一个str比较，直到loop所有strs。另外DC（把所有str分成两份，left和right处理），Binary Search（把首str二分处理）等，但是implementation会比较复杂。
注意Helper function的reference需要在assignment之后，所以要写在前面。
# Topics
- helper function