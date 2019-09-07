# Summary
Difficulty: Easy<br/>
[Link to problem](https://leetcode.com/problems/palindrome-number/)<br/>
## sol1: 84ms(27.6%)
## sol2: 100ms
Even slower for simplifed code. Next, try not to break integer into string.
## sol3: 76ms
Use % to retrive the last digit in x, and build reverted x from scratch. x is also losting its trailing digits, while maintain the front half by the end of loop.
## sol4: 56ms(97% python3 one-liner)
[Double colons, use it to reverse list](https://stackoverflow.com/questions/3453085/what-is-double-colon-in-python-when-subscripting-sequences)<br/>
Use double colon to skip-pick items in a list. Can also be used to reverse list. For example, string -> gnirts
# Topics
- Math
- % and /
- Double colons