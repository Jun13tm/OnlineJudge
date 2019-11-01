# Overview
- Star
- Medium
- [Link to problem](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

## sol1: 90%
难点在于需要remove curr前面的nodes。<br>
另外，无重复时不remove，有重复时remove all，所以需要keep一个counter。如果要用helper
method的话，使用nonlocal去modify parent.

## sol2: 
while的写法略微不同。

# Topics
- linkedlist