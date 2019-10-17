# Overview
- Easy
- [Link to problem](https://leetcode.com/problems/implement-strstr/)

## sol1: 57%
Edge case需要handle无needle(恒定0)，和needle大于haystack(恒定-1)两种情况。在outer for loop里处理out of bound的情况。

# Topics
- array
- two_pointers