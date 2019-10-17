# Overview
- Easy
- [Link to problem](https://leetcode.com/problems/valid-parentheses/)

## sol1: 79%
用dictionary match不同种类的括号。如果是合理的closing parenthesis，stack.pop()，其他情况则stack.append()。loop结束以后检查stack是否为空。

# Topics
- stack
- array